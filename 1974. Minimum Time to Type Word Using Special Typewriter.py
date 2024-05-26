class Solution:
    def minTimeToType(self, word: str) -> int:
        # 26 - 23 = 3
        # 4 - 1 = 3

        # abs(curr - target)
        # if > 12:
        # 26 - 

        # ord - 96
        time = 0
        pointer = 1
        curr = pointer
        for char in word:
            target = ord(char) - 96
            distance = abs(curr - target)
            if distance > 13:
                distance = 26 - distance

            curr = target
            time += distance + 1
        
        return time

