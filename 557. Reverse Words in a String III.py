class Solution:
    def reverseWords(self, s: str) -> str:
        words: List[str] = s.split(' ')
        words = (word[::-1] for word in words)
        return ' '.join(words)
        
