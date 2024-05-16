class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        output = []
        for element in evens:
            output.append(element)
        for element in odds:
            output.append(element)
        return output

