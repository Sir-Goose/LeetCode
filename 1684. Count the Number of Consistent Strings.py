class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count: int = 0

        for word in words:
            consistent = True
            for letter in word:
                if letter not in allowed:
                    consistent = False
            
            if consistent:
                count += 1

        return count
        
