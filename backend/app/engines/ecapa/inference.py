class ECAPAInference:
    """Inference logic for ECAPA speaker verification."""

    def predict(self, embedding: list[float]) -> float:
        return sum(embedding) / max(len(embedding), 1)
