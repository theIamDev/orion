from typing import AsyncGenerator
from packages.filesystem.fileSystemController import FileSystemController

class RepositoryService:
    def __init__(self, fs_package: FileSystemController = None):
        self.fs_package = fs_package or FileSystemController()

    async def process_document_upload(self, filename: str, stream: AsyncGenerator[bytes, None]) -> str:
        """Service: Executes core application business rules and domain workflows."""
        
        # Example Business Rule: Validate file names or structure logic
        if len(filename) > 255:
            raise ValueError("Filename exceeds safe database limits.")

        # Direct the underlying infrastructure package to write the validated stream
        saved_path = await self.fs_package.upload_document(filename, stream)
        return saved_path