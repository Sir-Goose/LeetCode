class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = {}
        for letter in s:
            if letter in count:
                return letter
            else:
                count[letter] = True

