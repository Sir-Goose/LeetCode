class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 3:
            n = n / 3

        return n == 3 or n == 1
