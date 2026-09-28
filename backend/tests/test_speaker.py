from app.services.speaker_identity import SpeakerIdentityService


def test_speaker_identity_service() -> None:
    service = SpeakerIdentityService()
    result = service.match("sample.wav", "speaker-1")
    assert "speaker_match_score" in result
