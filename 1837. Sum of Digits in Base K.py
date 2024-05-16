class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return '0'
        result = ''
        while n > 0:
            n, remainder = divmod(n, k)
            result = str(remainder) + result
        
        total = 0
        for char in result:
            total += int(char)
        
        return total

