class AASISTInference:
    """Inference logic for AASIST."""

    def predict(self, features: list[float]) -> float:
        return sum(features) / max(len(features), 1)
