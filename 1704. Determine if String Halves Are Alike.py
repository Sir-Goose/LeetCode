class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels: List[str] = ['a', 'e', 'i', 'o', 'u'] 
        count1: int = 0
        count2: int = 0
        midpoint: int = len(s) / 2
        midpoint = int(midpoint)

        s = s.lower()
        half1: str = s[:midpoint]
        half2: str = s[midpoint:]

        for char in half1:
            if char in vowels:
                count1 += 1
        for char in half2:
            if char in vowels:
                count2 += 1

        return count1 == count2
        

