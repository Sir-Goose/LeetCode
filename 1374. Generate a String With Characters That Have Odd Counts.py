class Solution:
    def generateTheString(self, n: int) -> str:
        output: str = ''
        for i in range(n - 1):
            output += 'a'

        if len(output) % 2 == 0:
            output += 'a'
        else:
            output += 'z'

        return output

