class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [0] * len(s)
        indices = []
        for i in range(len(s)):
            if s[i] == c:
                indices.append(i)
        for i in range(len(s)):
            distance = 1001
            for j in range(len(indices)):
                distance = min(abs(i - indices[j]), distance)
            answer[i] = distance

        return answer

