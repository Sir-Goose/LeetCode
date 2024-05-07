class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if i % 2 != 0:
                s[i] = self.shift(s[i-1], int(s[i]))

        return ''.join(_ for _ in s)
        
    def shift(self, c, x):
        return chr(ord(c) + x)

