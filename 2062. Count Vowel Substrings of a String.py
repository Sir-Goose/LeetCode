class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = 'aeiou'
        

        substrings = []
        for i in range(0, len(word)):
            for j in range(0, len(word)-i):
                window = word[j:j+i+1]
                if set(window) == set(vowels):
                    substrings.append(window)
                
        return len(substrings)

