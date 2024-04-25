class Solution:
    def minimumSum(self, num: int) -> int:
        str_num = str(num)
        sorted_num = sorted(str_num)
        
        num1 = ''
        num2 = ''

        num1 += sorted_num[0]
        num2 += sorted_num[1]
        num1 += sorted_num[2]
        num2 += sorted_num[3]

        print(f'{num1} {num2}')

        return int(num1) + int(num2)

