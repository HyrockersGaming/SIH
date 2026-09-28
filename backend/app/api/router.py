from fastapi import APIRouter

from app.api.routes import (
    context,
    health,
    risk,
    scenarios,
    security,
    speaker,
    voice,
)

api_router = APIRouter()
api_router.include_router(health.router, prefix="/api", tags=["health"])
api_router.include_router(voice.router, prefix="/api/voice", tags=["voice"])
api_router.include_router(speaker.router, prefix="/api/speaker", tags=["speaker"])
api_router.include_router(context.router, prefix="/api/context", tags=["context"])
api_router.include_router(risk.router, prefix="/api/risk", tags=["risk"])
api_router.include_router(scenarios.router, prefix="/api/scenarios", tags=["scenarios"])
api_router.include_router(security.router, prefix="/api/security", tags=["security"])
