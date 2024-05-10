class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_sum = 0
        for word in words:
            good = True
            for char in word:
                if word.count(char) <= chars.count(char):
                    pass
                else:
                    good = False
            if good:
                good_sum += len(word)

        return good_sum

