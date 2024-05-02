class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []

        for i in range(len(grid)):
            one_count = 0
            zero_count = 0
            for item in grid[i]:
                if item == 1:
                    one_count += 1
                elif item == 0:
                    zero_count += 1
            onesRow.append(one_count)
            zerosRow.append(zero_count)

        for j in range(len(grid[0])):
            one_count = 0
            zero_count = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    one_count += 1
                elif grid[i][j] == 0:
                    zero_count += 1
            onesCol.append(one_count)
            zerosCol.append(zero_count)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        print(onesRow)
        print(onesCol)
        print(zerosRow)
        print(zerosCol)

        return grid 

