from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from .controllers.repositoryController import RepositoryController

REPOSITORY_ROUTER = APIRouter()

@REPOSITORY_ROUTER.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Route: Exposes the HTTP endpoint and handles network exceptions."""
    try:
        # Pass the framework payload directly to the Controller layer
        result = await RepositoryController().handle_upload(file)
        return result
        
    except ValueError as ve:
        # Route translates standard application exceptions into exact HTTP status codes
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


