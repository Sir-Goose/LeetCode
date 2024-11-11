class Solution:
    def stringSequence(self, target: str) -> List[str]:
        output = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        prev = ""
        for char in target:
            count = 0
            while count < len(letters):
                if letters[count] == char:
                    sequence = prev + letters[count]
                    output.append(sequence)
                    prev = sequence
                    break
                else:
                    output.append(prev+letters[count])
                count += 1

        return output
