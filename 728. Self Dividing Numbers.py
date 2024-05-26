class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        
        for i in range(left, right+1):
            digits = list(str(i))
            if '0' in digits:
                continue
            divides = True
            for digit in digits:
                if i % int(digit) != 0:
                    divides = False
            if divides:
                output.append(i)
        
        return output
                    

