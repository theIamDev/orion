from typing import AsyncGenerator
from fastapi import UploadFile
from ..services.repositoryService import RepositoryService

class RepositoryController:
    def __init__(self, fs_service: RepositoryService = None):
        self.fs_service = fs_service or RepositoryService()

    async def handle_upload(self, file: UploadFile) -> dict:
        """Controller: Converts framework Web data types into clean Python streams."""
        filename = file.filename
        if not filename:
            raise ValueError("Invalid file: Missing filename.")

        # Construct the asynchronous stream chunk generator out of FastAPI's file handle
        async def file_chunk_generator() -> AsyncGenerator[bytes, None]:
            try:
                while chunk := await file.read(1024 * 1024):  # 1MB Chunks
                    yield chunk
            finally:
                await file.close()  # Safely free up system temporary file descriptors

        # Hand off clean data (filename string and raw stream) to the Business Service
        saved_path = await self.fs_service.process_document_upload(filename, file_chunk_generator())
        
        return {"message": "File uploaded successfully", "path": saved_path}