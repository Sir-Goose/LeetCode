class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        output = [False] * m
        
        for i in range(m):
            start, end = l[i], r[i]
            sequence = nums[start: end + 1]
            sequence = sorted(sequence)
            output[i] = self.is_constant(sequence)
        
        return output
            
            
    def is_constant(self, sequence):
        print(sequence)
        diff = sequence[1] - sequence[0]
        for j in range(2, len(sequence)):
            if sequence[j] - sequence[j-1] != diff:
                return False
        return True

