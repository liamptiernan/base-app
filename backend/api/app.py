from fastapi import FastAPI
from backend.api.routes import users

app = FastAPI()

prefix = "/api/v1"
app.include_router(users.router, prefix=prefix)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"message": "OK"}
