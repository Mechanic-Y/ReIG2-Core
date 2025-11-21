from typing import Dict, Tuple, List
from ..sensitive_scanner import SensitiveScanner

class SafetyPolicy:
    RANK_A = "A: High Confidence"
    RANK_B = "B: Medium Confidence"
    RANK_C = "C: Low Confidence"

    def __init__(self):
        self.scanner = SensitiveScanner()

    def gate1_check(self, text: str) -> Tuple[bool, str]:
        return self.scanner.scan(text)

    def gate2_verify(self, response_text: str, citations: List[str]) -> Dict:
        verification_result = {"is_valid": True, "rank": self.RANK_B, "issues": []}
        if not citations:
            verification_result["rank"] = self.RANK_C
        elif len(citations) >= 2:
            verification_result["rank"] = self.RANK_A
        return verification_result

    def get_safe_response(self, category: str) -> str:
        return f"Safety Policy Violation: Cannot provide instructions regarding {category}."