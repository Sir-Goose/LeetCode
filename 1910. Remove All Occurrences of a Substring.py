class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            try:
                index = s.index(part)
                s = s[:index] + s[index+len(part):]
            except:
                return s
                
            
