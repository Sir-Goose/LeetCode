class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        counter = 0
        XOR = None
        for num in nums:
            if XOR:
                XOR = XOR ^ num
                k = XOR ^ (2 ** maximumBit - 1)
            else:
                XOR = num
                k = XOR ^ (2 ** maximumBit - 1)
            answer.append(k)
        
        return answer[::-1]

