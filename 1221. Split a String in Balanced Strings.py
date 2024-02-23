class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count: int = 0
        r_count: int = 0

        maximum_strings: int = 0
        
        for character in s:
            if character == 'L':
                l_count += 1
            if character == 'R':
                r_count += 1
            if l_count == r_count:
                maximum_strings += 1
                l_count = 0
                r_count = 0
        
        return maximum_strings
            
