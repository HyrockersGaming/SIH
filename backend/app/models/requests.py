from pydantic import BaseModel, Field


class VoiceVerificationRequest(BaseModel):
    audio_path: str = Field(..., description="Path to the input audio file")
    speaker_id: str | None = Field(default=None, description="Known speaker identifier")
