import aiofiles
import aiofiles.os
from pathlib import Path
from typing import AsyncGenerator
from packages.filesystem.baseConnector import BaseConnector

DEFAULT_BASE_PATH = "E:/workspace/codes/iamdev/data" 

class LocalFileSystemConnector(BaseConnector):

    def __init__(self, base_path: str = DEFAULT_BASE_PATH):
        self.base_path = Path(base_path).resolve()
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _get_full_path(self, file_path: str) -> Path:
        full_path = (self.base_path / file_path).resolve()
        if not str(full_path).startswith(str(self.base_path)):
            raise PermissionError("Directory traversal detected: Access denied.")
        return full_path

    async def download_stream(self, filename: str) -> AsyncGenerator[bytes, None]:
        """Reads a file asynchronously in 1MB chunks to keep RAM usage minimal."""
        full_path = self._get_full_path(filename)
        
        if not full_path.exists():
            raise FileNotFoundError(f"File not found: {full_path}")

        # 'rb' ensures we are strictly speaking in bytes!
        async with aiofiles.open(full_path, "rb") as file:
            while chunk := await file.read(1024 * 1024):  # Yield 1MB at a time
                yield chunk

    async def upload_stream(self, filename: str, stream: AsyncGenerator[bytes, None]) -> str:
        """Writes a file asynchronously by consuming a byte stream."""
        full_path = self._get_full_path(filename)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 'wb' ensures we are strictly writing bytes!
        async with aiofiles.open(full_path, "wb") as file:
            async for chunk in stream:
                await file.write(chunk)
                
        return str(full_path)

    async def delete_file(self, file_path: str) -> None:
        """Deletes a file asynchronously."""
        full_path = self._get_full_path(file_path)
        if full_path.exists():
            # Use aiofiles.os to prevent blocking the event loop during deletion
            await aiofiles.os.remove(full_path) 
        else:
            raise FileNotFoundError(f"File not found at: {full_path}")