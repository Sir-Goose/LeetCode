class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count: int = 0

        for sentence in sentences:
            words: int = 0
            for character in sentence:
                if character == ' ':
                    words += 1
            count = max(count, words + 1)

        return count
        
