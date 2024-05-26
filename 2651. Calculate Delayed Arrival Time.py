class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        new_time = arrivalTime + delayedTime
        if new_time < 24:
            return new_time
        if new_time == 24:
            return 0
        else:
            return new_time - 24
        
