from packages.documentparse.documentParseController import parser_controller
from packages.filesystem.fileSystemController import filesystem_controller

async def parse_document(filename: str):
    try:
        file_bytes = await filesystem_controller.read_file(filename)
        return await parser_controller.process_document(file_bytes, filename)
    except Exception as e:
        raise Exception(f"Document parsing failed: {str(e)}")