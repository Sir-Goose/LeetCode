class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
        
        if len(output) > 0:
            output = sorted(output)
            return output
        else:
            return output

