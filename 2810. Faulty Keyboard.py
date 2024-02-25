class Solution:
    def finalString(self, s: str) -> str:
        output: str = ""
        for character in s:
            if character == 'i':
                output = output[::-1]
            else:
                output = output + character
        
        return output

