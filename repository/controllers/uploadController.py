from typing import AsyncGenerator
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from packages.filesystem.fileSystemController import FileSystemController

upload_router = APIRouter()

# We use FastAPI's Depends to manage the controller lifecycle cleanly
def get_fs_controller() -> FileSystemController:
    return FileSystemController()

@upload_router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    fs_controller: FileSystemController = Depends(get_fs_controller)
):
    """Uploads a file to the specified destination path using memory-safe streaming."""
    try:
        filename = file.filename
        if not filename:
            raise HTTPException(status_code=400, detail="Invalid file: Missing filename.")

        # 1. Define an inner async generator to read FastAPI's UploadFile in chunks
        async def file_chunk_generator() -> AsyncGenerator[bytes, None]:
            try:
                while chunk := await file.read(1024 * 1024):  # 1MB Chunks
                    yield chunk
            finally:
                # Always close the FastAPI UploadFile to free up system temp resources
                await file.close()

        # 2. Await the streaming transfer to the controller
        saved_path = await fs_controller.upload_document(filename, file_chunk_generator())
        
        return {"message": "File uploaded successfully", "path": saved_path}
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")