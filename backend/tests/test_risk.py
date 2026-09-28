from app.services.risk_engine import RiskEngineService


def test_risk_engine_service() -> None:
    service = RiskEngineService()
    result = service.score(0.9, 0.8, 0.7)
    assert result["risk_level"] in {"Low", "Medium", "High"}
    assert result["decision"] in {"Accept", "Review", "Reject"}
