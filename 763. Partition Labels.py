class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = []
        i = 1
        while(s):
            print(s)
            if len(s) == 0:
                break
            if len(set(s[:i]) & set(s[i:])) == 0:
                parts.append(s[:i])
                s = s[i:]
                i = 1
            else:
                i += 1
                if i == len(s):
                    parts.append(s)
                    break
        
        return [len(_) for _ in parts]
                
