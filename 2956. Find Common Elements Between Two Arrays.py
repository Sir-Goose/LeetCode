class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [0, 0]
        n, m = len(nums1), len(nums2)

        for i in range(n):
            if nums1[i] in nums2:
                output[0] += 1
                
        for i in range(m):
            if nums2[i] in nums1:
                output[1] += 1
        
        return output

