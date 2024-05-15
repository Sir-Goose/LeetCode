class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0 
        while len(grid[0]) > 0:
            print(grid)
            deleted_elements = []
            for i in range(len(grid)):
                max_element = max(grid[i])
                grid[i].remove(max_element)
                deleted_elements.append(max_element)
            answer += max(deleted_elements)
        return answer

