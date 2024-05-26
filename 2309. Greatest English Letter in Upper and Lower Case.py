class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = []
        lower = []
        
        for letter in s:
            if letter.isupper():
                upper.append(letter)
            else:
                lower.append(letter.upper())
        contenders = set(upper) & set(lower)
        print(contenders)
        contenders = sorted(contenders)
        if contenders:
            return contenders[-1]
        else:
            return ''

