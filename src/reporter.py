"""Report Generator"""
class ReportGenerator:
    def markdown(self, token: str, score: dict) -> str:
        b=score["breakdown"]
        return f"""## {token}: {score['rating']} ({score['total']}/100)
| Metric | Score |
|---|---|
"""+"\n".join(f"| {k.title()} | {v} |" for k,v in b.items())+f"""\n\n**Recommendation:** {score['rating']}"""
    def batch_report(self, results: list) -> str: return "\n---\n".join(self.markdown(r.get("name","Unknown"), r["score"]) for r in results)
