import asyncio
from io import BytesIO
from docling.datamodel.base_models import InputFormat, DocumentStream
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from ..documentParserConnector import DocumentParserConnector

class DoclingConnector(DocumentParserConnector):
    def __init__(self, device: str = "cpu"):
        self.device = device

        pdf_options = PdfPipelineOptions()
        pdf_options.do_ocr = False  # No OCR

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pdf_options
                )
            }
        )

    async def parse_bytes(self, file_bytes: bytes, file_extension: str) -> str:
        """Asynchronously parses raw document bytes using local Docling engine."""
        print(f"Starting docling parser for extension: {file_extension}")

        # 1. Map the string file_extension to Docling's expected InputFormat enum
        # Normalize the extension to lowercase and remove leading dot if necessary
        ext = file_extension.lower().lstrip(".")
        
        if ext == "pdf":
            input_format = InputFormat.PDF
        elif ext in ["docx", "doc"]:
            input_format = InputFormat.DOCX
        else:
            # Fallback to generic text or let docling try auto-detect
            input_format = InputFormat.PDF 

        # 2. Prepare the in-memory streams
        binary_stream = BytesIO(file_bytes)
        source = DocumentStream(name=f"document.{ext}", stream=binary_stream)

        # 3. CRITICAL: Run the heavy CPU-bound parsing in a separate thread 
        # so it doesn't block the async event loop.
        result = await asyncio.to_thread(self.converter.convert, source)

        if result.document is None:
            raise RuntimeError("Docling could not parse the document bytes.")

        return result.document.export_to_markdown()