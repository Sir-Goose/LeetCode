class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for char in s:
            if char is letter:
                count += 1

        return int(count / len(s) * 100)

