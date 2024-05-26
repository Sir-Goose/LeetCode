class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
        
        for char in words[0]:
            common = True
            for i in range(len(words)):
                if char not in words[i]:
                    common = False
                else:
                    index = words[i].find(char)
                    words[i] = words[i][:index] + words[i][index+1:]

            if common:
                common_chars.append(char)
        return common_chars
        
