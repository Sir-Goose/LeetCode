class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_digits = 1
        sum_digits = 0
        for digit in str(n):
            product_digits *= int(digit)
            sum_digits += int(digit)

        return int(product_digits - sum_digits)

        
