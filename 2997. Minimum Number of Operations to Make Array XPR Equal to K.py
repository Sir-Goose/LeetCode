class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        
        xor = bin(xor)
        k = bin(k)

        k = k[2:]
        xor = xor[2:]

        print(k)
        print(xor)

        while len(k) < len(xor):
            k = '0' + k
        while len(k) > len(xor):
            xor = '0' + xor
        
        for i in range(len(xor)):
            if xor[i] != k[i]:
                count += 1

        return count
        
            
