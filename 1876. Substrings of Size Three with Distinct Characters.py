class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(3, len(s)+1):
            print(s[i-3:i])
            count += 1 if len(set(s[i-3:i])) == 3 else 0
        return count

