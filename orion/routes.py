from fastapi import APIRouter
from  repository.routes import REPOSITORY_ROUTER

MAIN_ROUTER = APIRouter()

MAIN_ROUTER.include_router(REPOSITORY_ROUTER, tags=["Repository"])

@MAIN_ROUTER.get("/")
def read_root():
    return {"message": "Welcome to your File Management API!", "status": "running"}