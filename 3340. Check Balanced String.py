class Solution:
    def isBalanced(self, num: str) -> bool:
        total: int = 0
        for i in range(len(num)):
            if (i % 2 == 0):
                total+= int(num[i])
            else:
                total -= int(num[i])

        return total == 0
