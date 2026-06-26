from abc import ABC, abstractmethod

class DocumentParserConnector(ABC):
    """Abstract interface defining the contract for both local and cloud-based 
    document extraction engines.
    """

    @abstractmethod
    async def parse_bytes(self, file_bytes: bytes, file_extension: str) -> str:
        """Parses raw document bytes and extracts text and structured data.

        Args:
            file_bytes: The raw binary data fetched from the storage connector.
            file_extension: The file type extension (e.g., '.pdf', '.docx') 
                            to hint the underlying parsing engine.

        Returns:
            A standardized string containing the extracted text (ideally Markdown).
        """
        pass