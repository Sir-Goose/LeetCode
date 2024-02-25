class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        pieces = []
        while True:
            left = 0
            right = 0

            for i in range(len(s)):
                if s[i] == '(':
                    left += 1
                if s[i] == ')':
                    right += 1
                if left == right:
                    pieces.append(s[:i + 1])
                    s = s[i + 1:]
                    break
            if len(s) == 0:
                break
            
        for i in range(len(pieces)):
            pieces[i] = pieces[i][1:-1]

        s = ''.join(pieces)
        return s
            
