class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                # check if strong
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    # if strong check xor val
                    xor = nums[i] ^ nums[j]
                    if xor > max_xor:
                        max_xor = xor
        return max_xor

