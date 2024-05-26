class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find the power set
        # OR each set

        n = len(nums)
        power_set = []

        for i in range(2**n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            power_set.append(subset)
        

        # find max OR
        max_or = 0
        for subset in power_set:
            if len(subset) > 0:
                OR = 0
                for num in subset:
                    OR = OR | num
                max_or = max(max_or, OR)

        count = 0
        
        for subset in power_set:
            if len(subset) > 0:
                OR = 0
                for num in subset:
                    OR = OR | num
                if OR == max_or:
                    count += 1
        return count

