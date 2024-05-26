class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr = 0
        for change in gain:
            curr += change
            max_alt = curr if curr > max_alt else max_alt
        
        return max_alt
        
