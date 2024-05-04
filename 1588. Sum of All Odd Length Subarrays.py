class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        valid_lengths = []
        for i in range(len(arr)+1):
            if int(i % 2) != 0:
                valid_lengths.append(i - 1)
            
        for length in valid_lengths:
            start = 0
            end = length
            while end < len(arr):
                total += sum(arr[start:end+1])
                start += 1
                end += 1
        
        return total

