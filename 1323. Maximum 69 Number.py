class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        list_num = list(str_num)
        if '6' not in list_num:
            return num
        
        if list_num[0] == '6':
            list_num[0] = '9'
            str_num = ''
            for i in range(len(list_num)):
                str_num += list_num[i]
            return int(str_num)
        
        
        for i in range(len(str_num)):
            if str_num[i] == '6':
                list_num[i] = '9'
                str_num = ''
                for i in range(len(list_num)):
                    str_num += list_num[i]
                return int(str_num)

