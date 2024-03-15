class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        index = -1
        
        s = s.strip()
        while True:
            try:
                if s[index] != ' ':
                    length += 1
                    index -= 1
                else:
                    return length
            except: 
                return length
