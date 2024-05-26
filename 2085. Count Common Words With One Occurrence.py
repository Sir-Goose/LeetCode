class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_dict = {}
        for word in words1:
            if word in words1_dict:
                words1_dict[word] += 1
            else:
                words1_dict[word] = 1
        words2_dict = {}

        for word in words2:
            if word in words2_dict:
                words2_dict[word] += 1
            else:
                words2_dict[word] = 1

        count = 0
        for key in words1_dict:
            if key in words2_dict:
                if words1_dict[key] == 1 and words2_dict[key] == 1:
                    count += 1
        return count
            
