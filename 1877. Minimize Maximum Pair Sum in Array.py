class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort list
        # pair biggest with smallest
        # move inwards 
        pairs = []
        nums = sorted(nums)
        for i in range(int(len(nums) / 2)):
            pairs.append([nums.pop(0), nums.pop()])
        
        max_sum = 0
        for pair in pairs:
            max_sum = max(sum(pair), max_sum) 
        
        return max_sum 
            
