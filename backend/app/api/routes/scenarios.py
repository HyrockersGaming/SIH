from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def scenario_status() -> dict[str, str]:
    return {"status": "scenario engine ready"}
