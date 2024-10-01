class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky = []
        memory = []
        for num in nums:
            if num in memory:
                sneaky.append(num)
            else:
                memory.append(num)
        return sneaky 


