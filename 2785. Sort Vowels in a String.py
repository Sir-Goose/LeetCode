class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        s = list(s)
        for i in range(len(s)):
            if ord(s[i]) == 97 or ord(s[i]) == 101 or ord(s[i]) == 105 or ord(s[i]) == 111 or ord(s[i]) == 117:
                vowels.append(ord(s[i]))
                s[i] = -1
                
            elif ord(s[i]) == 65 or ord(s[i]) == 69 or ord(s[i]) == 73 or ord(s[i]) == 79 or ord(s[i]) == 85:
                vowels.append(ord(s[i]))
                s[i] = -1
        
        vowels = sorted(vowels)
        for i in range(len(s)):
            if s[i] == -1:
                s[i] = chr(vowels.pop(0))
        
        output = ''.join(char for char in s)
        return output
            
