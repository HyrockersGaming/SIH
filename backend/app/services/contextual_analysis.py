class ContextualAnalysisService:
    """Service for scenario and context evaluation."""

    def evaluate(self, scenario_id: str | None = None) -> dict[str, float | list[str]]:
        return {"context_score": 0.7, "suspicious_signals": []}
