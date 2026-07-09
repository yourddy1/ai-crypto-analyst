# AI Crypto Analyst 📊
Scoring engine — 50+ metrics across liquidity, volume, community, narrative, risk.

```python
from src.scorer import CryptoScorer
scorer = CryptoScorer()
result = scorer.score({"liquidity":0.95,"volume":0.88,"holders":0.72,"community":0.65,"narrative":0.80,"risk":0.12})
print(result["rating"])
```
MIT © yourddy1