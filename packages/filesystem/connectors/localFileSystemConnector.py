

from pathlib import Path
from packages.filesystem.baseConnector import BaseConnector

BASE_PATH = "E:/workspace/codes/iamdev/data" 

class LocalFileSystemConnector(BaseConnector):

    def __init__(self):
        self.base_path = Path(BASE_PATH).resolve()
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _get_full_path(self, file_path: str) -> Path:
        full_path = (self.base_path / file_path).resolve()
        if not str(full_path).startswith(str(self.base_path)):
            raise PermissionError("Directory traversal detected: Access denied.")
        return full_path

    def read_file(self, file_path: str, binary: bool = True) -> bytes | str:
        full_path = self._get_full_path(file_path)
        mode = "rb" if binary else "r"
        with open(full_path, mode) as file:
            return file.read()

    def write_file(self, filename: str, content: bytes | str, binary: bool = True) -> str:
        full_path = self._get_full_path(filename)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        mode = "wb" if binary else "w"
        with open(full_path, mode) as file:
            file.write(content)
        return str(full_path)

    def delete_file(self, file_path: str) -> None:
        full_path = self._get_full_path(file_path)
        if full_path.exists():
            full_path.unlink()
        else:
            raise FileNotFoundError(f"File not found at: {full_path}")