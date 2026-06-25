from fastapi import  File, HTTPException, Query
from packages.filesystem.fileSystemController import FileSystemController


async def upload(file):
    try:
        fs_controller = FileSystemController()
        content =  await file.read()
        filename = file.filename
        saved_path = fs_controller.upload_document(filename, content)
        return {"message": "File uploaded successfully", "path": saved_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")