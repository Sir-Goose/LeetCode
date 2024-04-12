class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m = 1
        while True:
            if n * m % 2 == 0:
                return n * m
            else:
                m += 1

