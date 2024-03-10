class Solution:
    def sortString(self, s: str) -> str:
        result = []
        s = list(s)

        while len(s) > 0:
            result.append(sorted(s)[0])
            s.remove(sorted(s)[0])
        
        
            r = []
            for char in sorted(s):
                if result[-1] != char:
                    result.append(char)
                else:
                    r.append(char)
            print(result)
            s = r

            if len(s) > 0:
                result.append(sorted(s)[-1])
                s.pop(-1)

            r = []
            for char in sorted(s)[::-1]:
                if result[-1] != char:
                    result.append(char)
                else:
                    r.append(char)
                s = r


        print(result)
        return ''.join(result)
