from fastapi import FastAPI
from repository.routes.routes import router as repo_router

app = FastAPI(title="File Management API")

# Include the external routes
app.include_router(repo_router, tags=["repository"])

@app.get("/")
def read_root():
    return {"message": "Welcome to your File Management API!", "status": "running"}