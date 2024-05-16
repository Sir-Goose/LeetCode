class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 2 or len(nums) == 1:
            return -1
        else:
            return sorted(nums)[1]

