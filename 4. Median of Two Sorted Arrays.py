class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        for num in nums1:
            nums2.append(num)
        big_list = sorted(nums2)

        if len(big_list) % 2 == 0:
            return (big_list[len(big_list) // 2] + big_list[len(big_list) // 2 - 1]) / 2
        else:
            return big_list[len(big_list) // 2]

