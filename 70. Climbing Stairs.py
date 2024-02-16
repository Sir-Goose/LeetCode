class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1
        temp = 0

        for i in range(n):
            if i == 0:
                temp = 0
            elif i == 1:
                temp = 1
            temp = prev + curr
            prev = curr
            curr = temp
        
        return temp
