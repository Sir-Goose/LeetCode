class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return n * (n + 1) // 2  

        weeks = n // 7
        remain = n - weeks * 7
        t1 = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2
        t2 = (2 * weeks + remain + 1) * remain // 2

        return t1 + t2

