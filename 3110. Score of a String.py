class Solution:
    def scoreOfString(self, s: str) -> int:
        values = []
        score = 0
        for char in s:
            values.append(ord(char))
        for i in range(len(values) - 1):
            score += (abs(values[i] - values[i + 1]))

        return score


