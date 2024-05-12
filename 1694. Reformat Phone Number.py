class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        new_number = ''
        while len(number) > 4:
            if len(new_number) > 0:
                new_number = new_number + '-' + number[0:3]
            else:
                new_number = number[0:3]
            number = number[3:]
        print(new_number)
        print(number)

        if len(number) == 3 or len(number) == 2:
            new_number = new_number + '-' + number
        else:
            new_number = new_number + '-' + number[:2] + '-' + number[2:]
        
        if new_number.startswith('-'):
            new_number = new_number[1:]
        return new_number
        
