class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        elements = []
        for n in nums:
            if n in elements:
                return n
            else:
                elements.insert(0, n)

