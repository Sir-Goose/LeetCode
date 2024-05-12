class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s) > k):
            chunks = []
            for i in range(0, len(s), k):
                chunks.append(s[i:i+k])
            new_s = ''
            for chunk in chunks:
                new_sum = 0
                for char in chunk:
                    new_sum += int(char)
                new_s += str(new_sum)
            s = new_s

        return s
