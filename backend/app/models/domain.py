from pydantic import BaseModel, Field


class SpeakerProfile(BaseModel):
    speaker_id: str
    embedding: list[float] = Field(default_factory=list)


class RiskContext(BaseModel):
    scenario_id: str | None = None
    context_score: float = 0.0
    suspicious_signals: list[str] = Field(default_factory=list)
