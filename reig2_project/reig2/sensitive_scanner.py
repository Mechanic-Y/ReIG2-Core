import re

class SensitiveScanner:
    PATTERNS = {
        "harmful": r"(爆弾|毒物|殺害|自傷|違法薬物|ハッキング).*(作り方|方法|手順)",
        "adult": r"(アダルト|18禁).*",
        "political_extreme": r"(ヘイトスピーチ|差別).*"
    }

    def __init__(self):
        self.compiled = {k: re.compile(v) for k, v in self.PATTERNS.items()}

    def scan(self, text: str):
        for cat, pat in self.compiled.items():
            if pat.search(text):
                return False, cat
        return True, "safe"