from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI app!", "status": "running"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}