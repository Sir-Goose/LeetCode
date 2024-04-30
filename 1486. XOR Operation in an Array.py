class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [0] * n
        arr[0] = start
        output = start
        for i in range(1, n):
            arr[i] = start + 2 * i
            output = output ^ arr[i]
        
        return output
        
