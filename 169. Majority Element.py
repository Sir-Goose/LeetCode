class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checked_numbers = [] 
        for i in range(len(nums)):
            if nums[i] in checked_numbers:
                continue
            count = 0
            checked_numbers.append(nums[i])
            
            for j in range(len(nums)):
               if nums[i] == nums[j]:
                   count += 1
                   if count > len(nums) / 2:
                       return nums[i]
