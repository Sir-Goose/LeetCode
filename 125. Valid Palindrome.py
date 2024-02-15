class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2 = ''
        for i in range(len(s)):
            if s[i].isalnum():
                str2 = str2 + s[i]
        
        str2 = str2.lower()
        print(str2)
        if str2[::-1] == str2:
            return True
        
        return False
