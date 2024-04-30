class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        output = 0
        i = 0
        while i < len(nums) -1 :
            lower = min(nums[i], nums[i + 1])
            output += lower 
            i += 2
        return output
