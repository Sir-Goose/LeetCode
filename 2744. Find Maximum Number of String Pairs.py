class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count: int = 0
        skip_list: List[int] = []
        for i in range(len(words)):
            if i in skip_list:
                continue
            for j in range(len(words)):
                if j in skip_list:
                    continue
                if j == i:
                    continue
                if words[i] == words[j][::-1]:
                    skip_list.append(i)
                    skip_list.append(j)
                    count += 1
        
        return count
                
