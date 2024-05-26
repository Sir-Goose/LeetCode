class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        
        unique_sum = 0
        for key in elements:
            if elements[key] == 1:
                unique_sum += key
        return unique_sum

