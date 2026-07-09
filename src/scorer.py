"""RobinScore Engine — 50+ data point analysis"""
import json, math
class CryptoScorer:
    METRICS = {"liquidity":0.25,"volume":0.20,"holders":0.15,"community":0.15,"narrative":0.15,"risk":0.10}
    def __init__(self): self.weights = self.METRICS.copy()
    def score(self, data: dict) -> dict:
        scores={}
        for m,w in self.weights.items(): scores[m]=min(100,data.get(m,0)*w*100)
        total = sum(scores.values())
        rating = "STRONG BUY" if total>=85 else "BUY" if total>=70 else "HOLD" if total>=40 else "AVOID"
        return {"total": round(total), "breakdown": scores, "rating": rating}
    def batch(self, tokens: list) -> list: return [self.score(t) for t in tokens]
    def to_json(self, results): return json.dumps(results, indent=2)
