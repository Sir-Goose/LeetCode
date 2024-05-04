class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = mat
        m = len(matrix)  
        n = len(matrix[0])  

        for diagonal in range(m + n - 1):
            start_row = max(0, diagonal - n + 1)
            start_col = max(0, n - diagonal - 1)

            diag = []
            for i in range(min(diagonal + 1, m - start_row, n - start_col)):
                diag.append(matrix[start_row + i][start_col + i])
            diag.sort()
            for i in range(min(diagonal + 1, m - start_row, n - start_col)):
                matrix[start_row + i][start_col + i] = diag.pop(0)

        return matrix


