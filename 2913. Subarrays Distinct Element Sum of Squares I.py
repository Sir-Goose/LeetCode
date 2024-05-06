class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # sliding window of each possible size
        # count the unique elements
        distinct_values = []
        
        for i in range(1, len(nums) + 1):
            window_size = i
            for j in range(len(nums) - i + 1):
                window = nums[j: j+i]
                distinct_values.append(len(set(window)))
                
        
        output = 0
        for value in distinct_values:
            output += (value ** 2)
        return output

