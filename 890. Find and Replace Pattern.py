class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # lengths the same
        # lengths of the sets are the same
        result = []
        for word in words:
            word_to_pattern, pattern_to_word = {}, {}
            for char, pattern_char in zip(word, pattern):
                if (char not in word_to_pattern) and (pattern_char not in pattern_to_word):
                    word_to_pattern[char], pattern_to_word[pattern_char] = pattern_char, char
                elif word_to_pattern.get(char) != pattern_char or pattern_to_word.get(pattern_char) != char:
                    break
            else:
                result.append(word)
        return result

