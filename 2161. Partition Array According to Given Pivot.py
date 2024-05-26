class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, middle, after = [], [], []

        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot: 
                middle.append(num)
            else:
                after.append(num)
        
        output = []
        for num in before:
            output.append(num)
        for num in middle:
            output.append(num)
        for num in after:
            output.append(num)
        
        return output

