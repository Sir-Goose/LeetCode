class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        avg1 = sum(nums1) // len(nums1)
        avg2 = sum(nums2) // len(nums2)
        return avg2 - avg1
        
