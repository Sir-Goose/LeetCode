class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        output = []

        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        pos1 = alphabet.index(s[0])
        pos2 = alphabet.index(s[3])
        width = pos2 - pos1 + 1
        print(width)
        lowest_cell = max(int(s[1]), int(s[4]))
        highest_cell = min(int(s[1]), int(s[4]))


        num_cells = width * lowest_cell 

        print(num_cells)



        for j in range(pos1, pos2 + 1):
            for i in range(highest_cell, lowest_cell + 1):
                output.append(alphabet[j] + str(i))
        
        return output


