class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = str(bin(x))[2:]
        y = str(bin(y))[2:]

        while len(x) < len(y):
            x = '0' + x
        while len(y) < len(x):
            y = '0' + y
        print(f"X: {x} Y: {y}")
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        return count
                
