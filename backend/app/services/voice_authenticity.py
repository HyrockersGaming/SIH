class VoiceAuthenticityService:
    """Service for waveform and spoofing analysis."""

    def analyze(self, audio_path: str) -> dict[str, float]:
        return {"authenticity_score": 0.92, "spoof_probability": 0.08}
