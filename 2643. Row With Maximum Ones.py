class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ones = {}
        max_ones = 0
        for i in range(len(mat)):
            ones[i] = mat[i].count(1)
            max_ones = max(max_ones, mat[i].count(1))
        
        for key in ones:
            if ones[key] == max_ones:
                return [key, max_ones]

