class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
    
        for i in range(n - 2):
            for j in range(n - 2):
                for x in range(3):
                    for y in range(3):
                        maxLocal[i][j] = max(maxLocal[i][j], grid[i + x][j + y])
                    
        return maxLocal

