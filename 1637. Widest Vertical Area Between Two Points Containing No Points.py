class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        print(points)

        max_width = 0
        for i in range(len(points) - 1):
            if abs(points[i][0] - points[i + 1][0]) > max_width:
                max_width = abs(points[i][0] - points[i + 1][0])
        return max_width
