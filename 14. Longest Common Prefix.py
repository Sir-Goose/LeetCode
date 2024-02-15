class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs:
            if s == "":
                return ""
            while s and s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

