class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            position: int = word.index(ch)
            new_string = ""
            prefix = word[:position + 1]
            prefix = prefix[::-1]
            new_string = prefix + word[position + 1:]
            return new_string
        return word

        
