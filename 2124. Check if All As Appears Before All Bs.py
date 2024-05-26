class Solution:
    def checkString(self, s: str) -> bool:
        trap = ''
        for char in s:
            if char == 'a' and trap == 'set':
                return False

            if char == 'b':
                trap = 'set'
        return True

