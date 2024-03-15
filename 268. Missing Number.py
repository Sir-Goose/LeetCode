class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique_nums = []
        for number in nums:
            if number not in unique_nums:
                unique_nums.append(number)
        
        unique_nums = sorted(unique_nums)

        if unique_nums[-1] != len(unique_nums):
            return unique_nums[-1] + 1

        if unique_nums[0] == 0:
            unique_nums = [num + 1 for num in unique_nums]
            for i in range(len(unique_nums ) - 1):
                if unique_nums[i + 1] - unique_nums[i] != 1:
                    return unique_nums[i]

        else:

            print(unique_nums)
            for i in range(len(unique_nums ) - 1):
                if unique_nums[i + 1] - unique_nums[i] != 1:
                    return unique_nums[i] + 1

        return 0
