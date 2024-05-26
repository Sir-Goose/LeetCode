class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)

        gcd = 0
        for i in range(1, small + 1):
            if small % i == 0 and big % i == 0:
                gcd = i
        
        return gcd

