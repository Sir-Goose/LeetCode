class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        
        return nums[0] * nums[1] - nums[-1] * nums[-2]
                            

