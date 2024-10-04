class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts = date.split("-")
        for i in range(len(parts)):
            parts[i] = (bin(int(parts[i])))

        return "-".join(parts)
