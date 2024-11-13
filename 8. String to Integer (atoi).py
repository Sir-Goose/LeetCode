class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        number = ''
        s = s.strip()
        if len(s) == 0:
            return 0
        print(s)
        sign = ''
        if s[0] == '+':
            sign = s[0]
            s = s[1:]
        elif s[0] == '-':
            sign = '-'
            s = s[1:]
        else:
            sign = '+'
        print(s)
        if len(s) == 0:
            return 0

        while s[0] == '0' and len(s) > 1:
            s = s[1:]
        if s == '0':
            return 0
        print(s)

        for digit in s:
            if digit in numbers:
                print(f"digit: {digit}")
                number += digit
            else:
                break

        print(number)
        if len(number) > 0:
            number = int(number)
        else:
            return 0
        if sign == '-':
            number *= -1
        if number > (2 ** 31) - 1:
            return (2 ** 31) -1
        elif number < -2 ** 31:
            return -2 ** 31

        return number
