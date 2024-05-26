class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largest_rectangle = 0
        count = 0
        for rectangle in rectangles:
            largest_rectangle = max(min(rectangle[0], rectangle[1]), largest_rectangle)
        for rectangle in rectangles:
            if min(rectangle[0], rectangle[1]) >= largest_rectangle:
                count+= 1
        return count
        

