class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        
        for word in strs:
            try:
                max_value = max(int(word), max_value)
            except:
                max_value = max(len(word), max_value)
        
        return max_value
                
