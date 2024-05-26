class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            print(grid[i])
            print(grid[i][0])
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        
        for j in range(len(grid[0])):
            zero_count = 0
            one_count = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    one_count += 1
                else:
                    zero_count += 1
            if zero_count > one_count:
                for i in range(len(grid)):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
                
        
        score = 0
        for row in grid:
            print(row)
            binary_string = ''.join(str(_) for _ in row)
            decimal_value = int(binary_string, 2)
            score += decimal_value
        
        return score
        

