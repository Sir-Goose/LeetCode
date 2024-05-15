class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (self.num_bits(x), x))
        return arr

    def num_bits(self, input):
        input = bin(input)
        input = str(input)
        count = 0
        for char in input:
            if char == '1':
                count += 1
        return count

