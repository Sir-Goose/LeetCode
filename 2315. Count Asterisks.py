class Solution:
    def countAsterisks(self, s: str) -> int:
        # just use boolean that we flip everytime we come across |
        in_pair: bool = False
        count: int = 0

        for char in s:
            if char == '|':
                in_pair = not in_pair
            if char == "*" and not in_pair:
                count += 1
        
        return count

