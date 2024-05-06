class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append((2 * i) + 1)
        print(arr)
        
        target = sum(arr) / n
        print(target)
        distance = 0
        
        for number in arr:
            distance += abs(target - number)
            
        return int(distance / 2)

