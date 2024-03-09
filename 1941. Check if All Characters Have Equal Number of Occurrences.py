class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_dict = {}
        for character in s:
            if character in count_dict:
                count_dict[character] += 1
            else:
                count_dict[character] = 1
        

        current = count_dict[s[0]]
        for ting in count_dict:
            if count_dict[ting] != current:
                return False
            current = count_dict[ting]
        

        return True
