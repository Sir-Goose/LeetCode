class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        grid = []
        
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            grid.append(row)
        

        
        for index in indices:
            print(grid)
            for i in range(n):
                grid[index[0]][i] += 1
                
            for j in range(m):
                grid[j][index[1]] += 1
        
        print(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] % 2 != 0:
                    count += 1
        return count

