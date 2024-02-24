class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_count: int = 0
            
        for i in range(len(s)):
            if s[i] == ' ':
                space_count += 1
                if space_count == k:
                    return s[0 : i]
                
        return s

