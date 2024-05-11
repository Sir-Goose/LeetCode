class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')

        s1 = sorted(s1)
        s2 = sorted(s2)
        bad_words = []
        for i in range(1, len(s1)):
            if s1[i-1] == s1[i]:
                bad_words.append(s1[i])
        for i in range(1, len(s2)):
            if s2[i-1] == s2[i]:
                bad_words.append(s2[i])

        
        for bad_word in bad_words:
            while bad_word in s1:
                s1.remove(bad_word)
            while bad_word in s2:
                s2.remove(bad_word)
        
        
        common = set(s1) & set(s2)
        uncommon = []
        for word in s1:
            if word not in common:
                uncommon.append(word)
        for word in s2:
            if word not in common:
                uncommon.append(word)
        return uncommon

