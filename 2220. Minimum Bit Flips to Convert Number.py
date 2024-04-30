class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]

        while len(start) < len(goal):
            start = '0' + start
        while len(goal) < len(start):
            goal = '0' + goal
        print(f"X: {start} Y: {goal}")
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1
        return count
