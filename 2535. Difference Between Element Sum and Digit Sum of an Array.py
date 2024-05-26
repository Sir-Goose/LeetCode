class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for element in nums:
            element_sum += element
            for digit in str(element):
                digit_sum += int(digit)

        return abs(element_sum - digit_sum)
        
