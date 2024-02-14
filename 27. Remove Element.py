class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre_length = len(nums)
        k = pre_length
        i = 0
        while(i < len(nums)):
            print(i)
            if (nums[i] == val):
                nums.pop(i)
                k -= 1
                i -= 1
            i += 1

        return k
