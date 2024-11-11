class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        original_length = len(nums)
        for i in range(original_length):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))
