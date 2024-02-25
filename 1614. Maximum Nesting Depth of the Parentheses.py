class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth: int = 0
        curr: int = 0

        for char in s:
            if char == '(':
                curr += 1

            if char == ')':
                curr -= 1

            max_depth = max(max_depth, curr)
                
        return max_depth

