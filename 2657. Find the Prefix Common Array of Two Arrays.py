class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []

        for i in range(len(A)):
            C.append(len(set(A[:i+1]) & set(B[:i+1])))
            
        return C

