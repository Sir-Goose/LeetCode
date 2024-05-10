class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(len(distance)):
            if chr(i +97) in s:
                char = chr(i + 97)
                print(char)
                first_pos = 0
                second_pos = 0
                for j in range(len(s)):
                    if s[j] == char:
                        first_pos = j
                        break
                print(first_pos)
                for j in range(first_pos+1, len(s)):
                    if s[j] == char:
                        second_pos = j

                first_pos += 1
                print(first_pos)
                print(second_pos)
                if second_pos - first_pos != distance[i]:
                    return False
        return True

