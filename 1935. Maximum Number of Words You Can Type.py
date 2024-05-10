class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = len(words)
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    count -= 1
                    break
        return count

