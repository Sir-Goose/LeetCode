class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = []
        
        positives = [] 
        negatives = []
        length = len(nums)
        for i in range(length):
            if nums[i] > 0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])

        half_length = int(length / 2)
        for i in range(half_length):
            output.append(positives.pop(0))
            output.append(negatives.pop(0))

        return output

