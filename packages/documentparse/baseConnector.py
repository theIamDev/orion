from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


# ==========================================
# 1. STANDARDIZED OUTPUT CONTRACT
# ==========================================
@dataclass(frozen=True)
class ParserResult:
    """Standardized container for parsed document data.

    Ensures that regardless of whether Docling or Azure is used, the 
    resulting data structure perfectly matches what your database schema expects.
    """
    raw_text: str                # Markdown or plain text representation
    structured_json: dict[str, Any]  # Hierarchies, tables, forms, or layout bounding boxes


# ==========================================
# 2. ABSTRACT BASE CONNECTOR
# ==========================================
class DocumentParserConnector(ABC):
    """Abstract interface defining required behaviors for all document parsers
    (e.g., Docling, Azure Document Parser).
    """

    @abstractmethod
    def parse_bytes(self, file_bytes: bytes, file_extension: str) -> ParserResult:
        """Parses raw document bytes and extracts text and structured data.

        Args:
            file_bytes: The raw file data fetched from the Filesystem Package.
            file_extension: The file type extension (e.g., '.pdf', '.docx') 
                            to hint the underlying parsing engine.

        Returns:
            A standardized ParserResult object.
        """
        pass