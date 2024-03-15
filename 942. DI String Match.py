class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm  = []
        options = []
        length = len(s)
        for i in range(length + 1):
            options.append(i)

        for j in range(length):
            if s[j] == 'I':
                perm.append(options.pop(0))
            else:
                perm.append(options.pop(-1))
 
        perm.append(options[0])
            
        return perm

