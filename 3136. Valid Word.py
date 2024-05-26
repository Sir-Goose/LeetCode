class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) >= 3:
            if word.isalnum():
                word = word.lower()
                if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
                    has_consonants = False
                    consonants = 'bcdfghjklmnpqrstvwxyz'
                    for char in word:
                        if char in consonants:
                            has_consonants = True
                    if has_consonants:
                        return True

        return False

