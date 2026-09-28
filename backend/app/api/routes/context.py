from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def context_status() -> dict[str, str]:
    return {"status": "context analysis ready"}
