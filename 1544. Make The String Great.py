class Solution:
    def makeGood(self, s: str) -> str:
        changed = True
        while changed:
            changed = False
            for i in range(len(s)-1):
                if abs(ord(s[i]) - ord(s[i+1])) == 32:
                    s = s[:i] + s[i+2:]
                    changed = True
                    break
        return s

