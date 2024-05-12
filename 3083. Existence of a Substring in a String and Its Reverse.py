class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r = s[::-1]
        for i in range(1, len(s)):
            if (s[i-1] + s[i]) in r:
                return True
        return False

