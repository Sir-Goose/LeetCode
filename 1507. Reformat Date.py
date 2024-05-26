class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(' ')
        day = ''
        month = ''
        for char in date[0]:
            if char.isdigit():
                day += char
        if len(day) < 2:
            day = '0' + day
        if date[1] == 'Jan':
            month = '01'
        elif date[1] == 'Feb':
            month = '02'
        elif date[1] == 'Sep':
            month = '09'
        elif date[1] == 'Mar':
            month = '03'
        elif date[1] == 'Oct':
            month = '10'
        elif date[1] == 'Nov':
            month = '11'
        elif date[1] == 'Dec':
            month = '12'
        elif date[1] == 'Apr':
            month = '04'
        elif date[1] == 'May':
            month = '05'
        elif date[1] == 'Jun':
            month = '06'
        elif date[1] == 'Jul':
            month = '07'
        elif date[1] == 'Aug':
            month = '08'

        return date[2] + '-' + month + '-' + day
        
