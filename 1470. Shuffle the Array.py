class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = 0.5 * len(nums)
        pointer_1 = 0
        pointer_2 = int(n)

        ans = []

        for i in range(int(n)):
            ans.append(nums[pointer_1])
            ans.append(nums[pointer_2])
            pointer_1 += 1
            pointer_2 += 1
            
        return ans

        
