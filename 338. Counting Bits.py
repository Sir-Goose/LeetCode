class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            binary = bin(i)
            bin_string = str(binary)
            count = 0
            for char in bin_string:
                if char == '1':
                    count += 1
            output.append(count)

        return output

