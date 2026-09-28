from pydantic import BaseModel, Field


class VerificationResponse(BaseModel):
    authenticity_score: float = Field(..., ge=0.0, le=1.0)
    speaker_match_score: float = Field(..., ge=0.0, le=1.0)
    risk_level: str = Field(..., description="Low, Medium, or High")
    decision: str = Field(..., description="Accept, Review, or Reject")
