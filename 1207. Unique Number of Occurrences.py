class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurance_count = {}
        for value in arr:
            if value in occurance_count:
                occurance_count[value] += 1
            else:
                occurance_count[value] = 1
        
        occurances = []
        for key in occurance_count:
            occurances.append(occurance_count[key])

        return len(occurances) == len(set(occurances))

