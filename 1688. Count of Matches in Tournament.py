class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        n = n
        while n != 1:
            if n % 2 == 0:
                total += n / 2
                n = int(n / 2)
            else:
                total += (n - 1) / 2
                n = int((n - 1) / 2 + 1)

        return int(total)
            
            
