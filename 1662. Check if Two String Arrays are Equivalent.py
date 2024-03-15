class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1: str = ""
        string2: str = ""

        for word in word1:
            for char in word:
                string1 = string1 + char

        for word in word2:
            for char in word:
                string2 = string2 + char

        return string1 == string2
        
