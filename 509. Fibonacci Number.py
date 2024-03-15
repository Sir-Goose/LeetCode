class Solution:
    def fib(self, n: int) -> int:
        current = 1
        previous = 0 
        sum = 0

        for i in range(n + 1):
            if i == 0:
                sum = 0
            elif i == 1:
                sum = 1
            else:
                sum = current + previous
                previous = current
                current = sum

        return sum
