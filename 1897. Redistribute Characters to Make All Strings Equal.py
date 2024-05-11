class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_length = 0
        char_counts = {}
        for word in words:
            for char in word:
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
        for key in char_counts:
            if char_counts[key] % len(words) != 0:
                return False
        return True

