class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = {}
        t_count = {}
        
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1
        
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        difference = 0
        for key in s_count:
            difference += max(0, s_count[key] - t_count.get(key, 0))
        
        return difference
        
