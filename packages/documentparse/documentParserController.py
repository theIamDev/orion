from packages.documentparse.documentParserConnector import DocumentParserConnector
from packages.documentparse.connectors.doclingConnector import DoclingConnector

class DocumentParseController:

    def __init__(self, connector: DocumentParserConnector = None):
        """The controller accepts whatever active parser connector it is given via dependency injection.
        
        It has zero direct knowledge of local paths or specific cloud SDKs.
        """
        # If no connector is specified, default to the local Docling engine.
        # This makes it easy to inject an Azure or AWS Textract connector later.
        self._connector = connector or DoclingConnector(device="cpu")

    async def process_document(self, file_bytes: bytes, file_extension: str) -> str:
        """Asynchronously triggers the parsing sequence on the raw file bytes."""
        if not file_bytes:
            raise ValueError("Cannot parse an empty byte stream.")
            
        print(f"[DocumentParseController] Executing parsing sequence for extension '{file_extension}'...")
        
        # Await the non-blocking async parser operation
        result = await self._connector.parse_bytes(file_bytes, file_extension)
        return result