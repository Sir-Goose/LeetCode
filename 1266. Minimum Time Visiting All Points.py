class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            x1, x2 = points[i][0], points[i+1][0]
            y1, y2 = points[i][1], points[i+1][1]
            
            
            while(True):
                if x1 < x2 and y1 < y2:
                    x1 += 1
                    y1 += 1
                elif x1 > x2 and y1 > y2:
                    x1 -= 1
                    y1 -= 1
                elif x1 > x2 and y1 < y2:
                    x1 -= 1
                    y1 += 1
                elif x1 < x2 and y1 > y2:
                    x1 += 1
                    y1 -= 1
                elif x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                elif y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
                else:
                    break
                time += 1
                
        
        return time

