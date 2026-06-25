from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import Response

from packages.filesystem.fileSystemController import FileSystemController 
fs_controller = FileSystemController()

app = FastAPI(title="File Management API")


# 3. Define the endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to your File Management API!", "status": "running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a file to the specified destination path."""
    try:
        content = await file.read()
        filename = file.filename
        saved_path = fs_controller.upload_document(filename, content)
        return {"message": "File uploaded successfully", "path": saved_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@app.get("/download")
def download_file(file_path: str = Query(..., description="The path of the file to download")):
    """Downloads a file from the specified path."""
    try:
        content = fs_controller.download_document(file_path)
        
        # If content is a string, encode it back to bytes for the response
        if isinstance(content, str):
            content = content.encode("utf-8")
            
        return Response(content=content, media_type="application/octet-stream")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found or cannot be read: {str(e)}")


@app.delete("/remove")
def remove_file(file_path: str = Query(..., description="The path of the file to delete")):
    """Removes a file from the file system."""
    try:
        fs_controller.remove_document(file_path)
        return {"message": f"File at {file_path} removed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Deletion failed: {str(e)}")