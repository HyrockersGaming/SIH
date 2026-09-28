from pydantic import BaseModel, Field


class ValidationError(BaseModel):
    field: str
    message: str


def validate_audio_file(path: str) -> bool:
    return bool(path and path.strip())
