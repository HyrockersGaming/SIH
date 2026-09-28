from app.services.contextual_analysis import ContextualAnalysisService
from app.services.risk_engine import RiskEngineService
from app.services.speaker_identity import SpeakerIdentityService
from app.services.voice_authenticity import VoiceAuthenticityService


class VerificationService:
    """Combines all verification signals into one final decision."""

    def __init__(self) -> None:
        self.voice_authenticity = VoiceAuthenticityService()
        self.speaker_identity = SpeakerIdentityService()
        self.contextual_analysis = ContextualAnalysisService()
        self.risk_engine = RiskEngineService()

    def verify(self, audio_path: str, speaker_id: str | None = None, scenario_id: str | None = None) -> dict[str, str | float]:
        voice_result = self.voice_authenticity.analyze(audio_path)
        speaker_result = self.speaker_identity.match(audio_path, speaker_id)
        context_result = self.contextual_analysis.evaluate(scenario_id)

        authenticity_score = voice_result["authenticity_score"]
        speaker_match_score = speaker_result["speaker_match_score"]
        context_score = context_result["context_score"]

        risk_result = self.risk_engine.score(authenticity_score, speaker_match_score, float(context_score))
        return {
            "authenticity_score": authenticity_score,
            "speaker_match_score": speaker_match_score,
            "context_score": context_score,
            "risk_level": risk_result["risk_level"],
            "decision": risk_result["decision"],
        }
