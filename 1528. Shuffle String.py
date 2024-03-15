class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_list = [0] * len(indices)

        for i in range(len(indices)):
            shuffled_list[indices[i]] = s[i]
        
        shuffled_string = ""
        for letter in shuffled_list:
            shuffled_string = shuffled_string + letter
        
        return shuffled_string
