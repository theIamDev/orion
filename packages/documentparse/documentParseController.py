from baseConnector import DocumentParserConnector, ParserResult
from packages.documentparse.connectors.doclingConnector import DoclingConnector

CONNECTOR = DoclingConnector(device="cpu")

# ==========================================
# 1. CONTROLLER (The Package Orchestrator)
# ==========================================
class DocumentParseController:

    def __init__(self, connector: DocumentParserConnector):
        """The controller simply execution-wraps whatever active document parser 

        connector it is given. It handles parsing and format enforcement.
        """
        self._connector = connector

    def process_document(self, file_bytes: bytes, file_name: str) -> ParserResult:
        """Invoked by the Document Parser Layer worker to parse raw file bytes.
        
        It extracts the file extension automatically to give a hint to the 
        underlying connector engine.
        """
        if not file_bytes:
            raise ValueError("Cannot parse an empty byte stream.")

        # Extract the extension (e.g., 'invoice.pdf' -> '.pdf')
        import os
        _, file_extension = os.path.splitext(file_name.lower())
        
        print(f"[DocumentParseController] Executing parsing sequence for file type: {file_extension}")
        
        # Delegate the actual low-level heavy lifting to the injected connector
        result = self._connector.parse_bytes(file_bytes, file_extension)
        
        return result





