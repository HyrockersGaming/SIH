from app.services.voice_authenticity import VoiceAuthenticityService


def test_voice_authenticity_service() -> None:
    service = VoiceAuthenticityService()
    result = service.analyze("sample.wav")
    assert "authenticity_score" in result
    assert "spoof_probability" in result
