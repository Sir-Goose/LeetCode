class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        substring = ''
        for char in s:
            if char not in substring:
                substring += char
            else:
                count += 1
                substring = char

        return count
                
        
