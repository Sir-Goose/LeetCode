class Solution:
    def countDigits(self, num: int) -> int:
        sum = 0
        digits = str(num)
        for digit in digits:
            if num % int(digit) == 0:
                sum += 1
        
        return sum
        
