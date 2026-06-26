from abc import ABC, abstractmethod


class DocumentParserConnector(ABC):
    """Abstract interface defining required behaviors for all document parsers
    (e.g., Docling, Azure Document Parser).
    """

    @abstractmethod
    def parse_bytes(self, file_bytes: bytes, file_extension: str):
        """Parses raw document bytes and extracts text and structured data.

        Args:
            file_bytes: The raw file data fetched from the Filesystem Package.
            file_extension: The file type extension (e.g., '.pdf', '.docx') 
                            to hint the underlying parsing engine.

        Returns:
            A standardized ParserResult object.
        """
        pass