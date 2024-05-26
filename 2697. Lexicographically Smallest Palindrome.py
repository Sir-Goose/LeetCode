class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) // 2):
            if s[-i -1] != s[i]:
                smallest = min(s[-i - 1], s[i])
                s[-i - 1] = smallest
                s[i] = smallest
        str_s = ''
        for char in s:
            str_s += char
        return str_s
            
