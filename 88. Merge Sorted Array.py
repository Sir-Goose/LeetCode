class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for element in nums2: 
            nums1.append(element)

        for i in range(n):
            nums1.pop(m)

        for i in range(len(nums1) - 1):
            for j in range(len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    temp = nums1[j + 1]
                    nums1[j + 1] = nums1[j]
                    nums1[j] = temp
