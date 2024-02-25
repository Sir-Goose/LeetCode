class Solution:
    def sortSentence(self, s: str) -> str:
        words: List[str] = s.split(' ')
        words = sorted(words, key=lambda string: string[-1])
        return ' '.join([word[:-1] for word in words])
