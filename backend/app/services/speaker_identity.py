class SpeakerIdentityService:
    """Service for speaker embedding and matching."""

    def match(self, audio_path: str, speaker_id: str | None = None) -> dict[str, float]:
        return {"speaker_match_score": 0.95}
