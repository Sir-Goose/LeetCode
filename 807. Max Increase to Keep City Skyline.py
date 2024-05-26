class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        added_height = 0
        columns = []
        for i in range(len(grid)):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            columns.append(column)

        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in columns]

        for i in range(len(grid)):
            for j in range(len(grid)):
                added_height += min(row_maxes[i], col_maxes[j]) - grid[i][j]

        return added_height
