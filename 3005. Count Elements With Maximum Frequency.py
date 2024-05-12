class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        max_freq = 0
        for freq in freqs:
            max_freq = max(max_freq, freqs[freq])
        count = 0
        for num in nums:
            if freqs[num] == max_freq:
                count += 1
        return count

