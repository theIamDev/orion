from abc import ABC, abstractmethod
from typing import AsyncGenerator

class BaseConnector(ABC):
    """Abstract interface defining the contract for the active storage backend."""

    @abstractmethod
    async def download_stream(self, file_path: str) -> AsyncGenerator[bytes, None]:
        """Downloads a file asynchronously as a stream of raw bytes."""
        pass

    @abstractmethod
    async def upload_stream(self, file_path: str, stream: AsyncGenerator[bytes, None]) -> str:
        """Uploads a file chunk by chunk from an async byte generator and returns the storage path/URI."""
        pass

    @abstractmethod
    async def delete_file(self, file_path: str) -> None:
        """Asynchronously removes a file from the storage backend."""
        pass