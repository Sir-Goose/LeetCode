class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        output = [0] * len(pref)

        output[0] = pref[0]

        for i in range(1, len(pref)):
            output[i] = pref[i] ^ pref[i - 1]

        return output


