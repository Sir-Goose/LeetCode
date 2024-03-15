class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num_patterns: int = 0
        for pattern in patterns:
            if pattern in word:
                num_patterns += 1
        
        return num_patterns
