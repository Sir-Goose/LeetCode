class Solution:
    def minLength(self, s: str) -> int:
        changed = True
        while changed:
            length = len(s)
            s = s.replace('AB', '').replace('CD', '')
            if len(s) == length:
                return len(s)

