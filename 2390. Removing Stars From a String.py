class Solution:
    def removeStars(self, s: str) -> str:
        while True:
            pos = s.find('*')
            if pos != -1:
                first = s[:pos-1]
                second = s[pos+1:]
                s = first + second
            else:
                break
        return s
