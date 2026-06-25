from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT INTERFACE (The Connector Blueprint)
# ==========================================
class BaseConnector(ABC):
    """Abstract interface defining the contract for the active storage backend."""

    @abstractmethod
    def read_file(self, file_path: str, binary: bool = True) -> bytes | str:
        pass

    @abstractmethod
    def write_file(self, file_path: str, content: bytes | str, binary: bool = True) -> str:
        pass

    @abstractmethod
    def delete_file(self, file_path: str) -> None:
        pass