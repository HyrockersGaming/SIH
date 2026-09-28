from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_voice_features() -> dict[str, list[str]]:
    return {"features": ["authenticity_scan", "speaker_match", "context_risk"]}
