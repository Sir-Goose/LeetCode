class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1 = []
        a2 = []
        
        nums1_set = set(nums1)
        for num in nums1_set:
            if num not in nums2:
                a1.append(num)
        
        nums2_set = set(nums2)
        for num in nums2_set:
            if num not in nums1:
                a2.append(num)
        return [a1, a2]

