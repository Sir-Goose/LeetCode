class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        output = []
        for i in range(len(nums)):
            if i % 2 != 0:
               continue 
            freq = nums[i]
            try:
                val = nums[i+1]
                piece = [val] * freq
                decompressed.append(piece) 
            except:
                break
        
        for segment in decompressed:
            for number in segment:
                output.append(number)

        return output 


