class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        squares = {}
        
        for i in range(len(mat)):
            squares[f"{i}, {i}"] = mat[i][i]
        
        for j, k in zip(range(len(mat)), range(len(mat) -1, -1, -1)):
            squares[f"{j}, {k}"] = mat[j][k]
        
        
        return sum([squares[key] for key in squares])

