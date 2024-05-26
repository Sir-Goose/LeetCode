class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) != 0:
            nums = sorted(nums)
            alice = nums[0]
            bob = nums[1]
            arr.append(bob)
            arr.append(alice)

            nums = nums[2:]

        return arr
