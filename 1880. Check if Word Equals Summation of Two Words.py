class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = ''
        second = ''
        third = ''


        for char in firstWord:
            first += str(ord(char) -97)
        for char in secondWord:
            second += str(ord(char) -97)
        for char in targetWord:
            third += str(ord(char) -97)

        if int(first) + int(second) == int(third):
            return True
        return False
        
