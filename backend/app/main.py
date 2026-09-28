from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="T0RI Backend",
    version="1.0.0",
    description="Voice authenticity and speaker verification backend for T0RI.",
)

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "T0RI backend is running"}
