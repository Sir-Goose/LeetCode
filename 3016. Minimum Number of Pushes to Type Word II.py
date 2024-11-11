class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1

        sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))

        word_set = ''.join(sorted_chars)

        keys = [''] * 8
        loop = 0
        count = 0
        for i in range(len(word_set)):
            keys[i - loop * 8] += word_set[i]
            count += 1
            if count == 8:
                loop += 1
                count = 0

        print(keys)
        print(word)

        pushes = 0
        for char in word:
            for key in keys:
                if char in key:
                    pushes += key.find(char) + 1
        return pushes
