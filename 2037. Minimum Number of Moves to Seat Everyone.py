class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        
        distance = 0
        for i in range(len(seats)):
            distance += abs(seats[i] - students[i])
        
        return distance
        
