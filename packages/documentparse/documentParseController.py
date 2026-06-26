from packages.documentparse.connectors.doclingConnector import DoclingConnector

CONNECTOR = DoclingConnector(device="cpu")

class DocumentParseController:

    def __init__(self):
        self._connector = CONNECTOR

    def process_document(self, file_path: str) :
        if not file_path:
            raise ValueError("Cannot parse an empty byte stream.")
        print(f"[DocumentParseController] Executing parsing sequence...")
        result = self._connector.parse_bytes(file_path)
        return result





