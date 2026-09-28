from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def risk_status() -> dict[str, str]:
    return {"status": "risk engine ready"}
