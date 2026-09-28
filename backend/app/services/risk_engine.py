class RiskEngineService:
    """Risk scoring and decision logic."""

    def score(self, authenticity_score: float, speaker_match_score: float, context_score: float) -> dict[str, str | float]:
        total = (authenticity_score + speaker_match_score + context_score) / 3
        if total < 0.5:
            return {"risk_level": "High", "decision": "Reject", "score": total}
        if total < 0.8:
            return {"risk_level": "Medium", "decision": "Review", "score": total}
        return {"risk_level": "Low", "decision": "Accept", "score": total}
