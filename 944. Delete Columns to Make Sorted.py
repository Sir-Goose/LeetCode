class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        cols = [0] * len(strs[0]) 



        for i in range(1, len(strs)):
            for j in range(n):
                if ord(strs[i-1][j]) > ord(strs[i][j]):
                    cols[j] = 1
        
        return sum(cols)

