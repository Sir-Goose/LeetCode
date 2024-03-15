class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen_letters = []
        for letter in sentence:
            if letter not in seen_letters:
                seen_letters.append(letter)

        return len(seen_letters) is 26
