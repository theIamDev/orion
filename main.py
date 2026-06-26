from fastapi import FastAPI
from orion.routes import MAIN_ROUTER

app = FastAPI(title="File Management API")

app.include_router(MAIN_ROUTER)

