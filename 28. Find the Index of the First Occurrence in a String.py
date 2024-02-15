class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = i + len(needle) 

        while j <= len(haystack):
            if needle == haystack[i: j]:
                return i
            else:
                i += 1
                j += 1

        return -1
