class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(k):
            nums = sorted(nums)
            score += nums[-1]
            nums[-1] += 1
        return score
            
