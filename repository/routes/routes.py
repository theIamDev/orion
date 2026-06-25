from fastapi import APIRouter, UploadFile, File, HTTPException
from ..controllers.upload import upload
from ..controllers.document_parse import parse_document

# Initialize controller and router

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a file to the specified destination path."""
    try:
        result = await upload(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@router.post("/parse")
async def document_parse(filename: str):
    """Parses a document and returns the extracted content."""
    try:
        await parse_document(filename)
        return "Document parsing completed successfully."
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Document parsing failed: {str(e)}")