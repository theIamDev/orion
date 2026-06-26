from collections.abc import AsyncGenerator

from .connectors.localFileSystemConnector import LocalFileSystemConnector
from .baseConnector import BaseConnector

# CONNECTOR = LocalFileSystemConnector()

class FileSystemController:

    def __init__(self, connector: BaseConnector = None):
        self._connector = connector or LocalFileSystemConnector()

    async def upload_document(self, filename: str, content_stream: AsyncGenerator[bytes, None]) -> str:
        """Receives a stream of bytes and passes it directly to the active connector."""
        return await self._connector.upload_stream(filename, content_stream)

    async def download_document(self, filename: str) -> AsyncGenerator[bytes, None]:
        """Retrieves an async byte stream from the connector to stream back to the client."""
        return self._connector.download_stream(filename)

    async def remove_document(self, filename: str) -> None:
        """Asynchronously requests the connector to delete a file."""
        await self._connector.delete_file(filename)