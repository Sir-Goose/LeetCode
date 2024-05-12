class Solution:
    def minOperations(self, logs: List[str]) -> int:
        height = 0

        for log in logs:
            print(height)
            if log == '../' and height != 0:
                height += 1
            elif log == '../' and height == 0:
                height = 0
            elif log == './':
                height += 0
            else:
                height -= 1

        return abs(height)

