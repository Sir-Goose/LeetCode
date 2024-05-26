class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        if n % 2 == 0:
            for i in range(1, n+1, 2):
                output.append(i)
                output.append(-i)
        else:
            for i in range(1, n, 2):
                output.append(i)
                output.append(-i)
            output.append(0)
        
        return output

