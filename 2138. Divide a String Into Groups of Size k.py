class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = list(s)
        output = []
        while(s):
            temp = ""
            for i in range(k):
                try:
                    temp += s.pop(0)
                except:
                    if len(temp) > 0:
                        output.append(temp)
                        temp = ""
                    break
            if len(temp) > 0:
                output.append(temp)
        for i in range(k - len(output[-1])):
            output[-1] += fill
        return output
        
