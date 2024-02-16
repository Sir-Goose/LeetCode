class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = bin(n)
        n = n[2:]
        for char in n:
           if char == '1': 
               count += 1

        return count
