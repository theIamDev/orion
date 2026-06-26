from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from ..baseConnector import DocumentParserConnector


class DoclingConnector(DocumentParserConnector):
    def __init__(self, device: str = "cpu"):
        self.device = device

        pdf_options = PdfPipelineOptions()
        pdf_options.do_ocr = False  # Same as: docling --no-ocr

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pdf_options
                )
            }
        )

    # Required because DocumentParserConnector demands this method.
    # In your current flow, you are passing a file path here.
    def parse_bytes(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        print(f"Starting document parser: {path}")

        result = self.converter.convert(path)

        if result.document is None:
            raise RuntimeError("Docling could not parse this PDF.")

        return result.document.export_to_markdown()