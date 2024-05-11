class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        distances = []

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    distances.append(j-i)
        if not distances:
            return -1
        return max(distances) -1

