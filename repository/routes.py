from fastapi import APIRouter
from .controllers.uploadController import upload_router

REPOSITORY_ROUTER = APIRouter()

REPOSITORY_ROUTER.include_router(upload_router)