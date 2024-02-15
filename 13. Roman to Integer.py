class Solution:
    def romanToInt(self, s: str) -> int:
        size = 0
        skip = False

        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if s[i] == 'I':
                if s[min(i + 1, len(s) - 1)] == 'V':
                   size += 4
                   skip = True
                elif s[min(i + 1, len(s) - 1)] == 'X':
                   size += 9
                   skip = True
                else:
                    size += 1

            elif s[i] == 'X':
                if s[min(i + 1, len(s) - 1)] == 'L':
                    size += 40
                    skip = True
                elif s[min(i + 1, len(s) - 1)] == 'C':
                    size += 90
                    skip = True
                else:
                    size += 10
            
            elif s[i] == 'C':
                if s[min(i + 1, len(s) - 1)] == 'D':
                    size += 400
                    skip = True
                elif s[min(i + 1, len(s) - 1)] == 'M':
                    size += 900
                    skip = True
                else:
                    size += 100
            
            elif s[i] == 'V':
                size += 5
            elif s[i] == 'L':
                size += 50
            elif s[i] == 'D':
                size += 500
            elif s[i] == 'M':
                size += 1000

        return size
