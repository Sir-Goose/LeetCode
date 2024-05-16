class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        values = {}
        for item in items1:
            if item[0] in values:
                values[item[0]] += item[1]
            else:
                values[item[0]] = item[1]

        for item in items2:
            if item[0] in values:
                values[item[0]] += item[1]
            else:
                values[item[0]] = item[1]
        
        ret = []
        for key in values:
            ret.append([key, values[key]])
        ret.sort(key=lambda x: x[0])

        return ret

