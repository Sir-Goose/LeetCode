class Solution:
    def countKeyChanges(self, s: str) -> int:
        count: int = 0
        s = s.lower()
        try:
            curr = s[1]
            prev = s[0]
        except:
            return 0
        for i in range(len(s)):
            if i == 0:
                continue
            curr = s[i]
            if curr != prev:
                count += 1
            prev = curr
        
        return count

        
