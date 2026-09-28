from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def speaker_status() -> dict[str, str]:
    return {"status": "speaker service ready"}
