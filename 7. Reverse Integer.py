class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        digits = []
        for char in str_x:
            digits.append(char)
        digits.reverse()
        reverse_x = ''
        for digit in digits:
            reverse_x += digit
        print(reverse_x)
        while reverse_x[0] == '0' and len(reverse_x) > 1:
            reverse_x = reverse_x[1:]

        if x > 0:
            if int(reverse_x) > -2 ** 31 and int(reverse_x) < (2 ** 31) -1:
                return int(reverse_x)
            else:
                return 0
        else:
            if int(reverse_x) > -2 ** 31 and int(reverse_x) < (2 ** 31) -1:
                return int(reverse_x) * -1
            else:
                return 0
