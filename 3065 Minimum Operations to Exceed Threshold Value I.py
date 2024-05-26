class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        for num in nums:
            if num < k:
                ops += 1

        return ops
        
