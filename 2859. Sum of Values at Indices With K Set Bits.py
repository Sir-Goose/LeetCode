class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0

        for i in range(len(nums)):
            if len(str(bin(i)).replace('0', '').replace('b', '')) == k:
                sum += nums[i]

        return sum
