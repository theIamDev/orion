from .connectors.localFileSystemConnector import LocalFileSystemConnector

CONNECTOR = LocalFileSystemConnector()

class FileSystemController:

    def __init__(self):
        """The controller simply accepts whatever active connector it is given.

        It has zero knowledge of global configs, strings, or paths.
        """
        self._connector = CONNECTOR

    def upload_document(self, filename: str,content: bytes | str) -> str:
        return self._connector.write_file(filename, content, binary=True)

    def download_document(self, file_path: str) -> bytes | str:
        return self._connector.read_file(file_path, binary=True)

    def remove_document(self, file_path: str) -> None:
        self._connector.delete_file(file_path)