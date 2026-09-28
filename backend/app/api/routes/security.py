from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def security_status() -> dict[str, str]:
    return {"status": "security layer ready"}
