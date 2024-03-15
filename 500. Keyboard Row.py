class Solution:
    row1 = "qwertyuiopQWERTYUIOP"
    row2 = "asdfghjklASDFGHJKL"
    row3 = "zxcvbnmZXCVBNM"

    def check_word(self, word: str) -> bool:
        in_row1 = 0
        in_row2 = 0
        in_row3 = 0
        
        for char in word:
            if char in self.row1:
                in_row1 = 1
            if char in self.row2:
                in_row2 = 1
            if char in self.row3:
                in_row3 = 1
        
        one_row = in_row1 + in_row2 + in_row3
        
        return one_row == 1


    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        return_word_list = []

        for word in words:
            if self.check_word(word):
                return_word_list.append(word)

        return return_word_list
