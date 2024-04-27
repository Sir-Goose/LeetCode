class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        
        for i in range(len(queries)):
            circle = queries[i]
            for point in points:
                if math.sqrt(abs(math.pow((circle[0] - point[0]), 2) + math.pow((circle[1] - point[1]), 2))) <= circle[2]:
                    answer[i] += 1
            
        return answer



