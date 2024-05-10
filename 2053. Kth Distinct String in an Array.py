class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        for word in arr:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
        ordered_distincts = []
        for key in counts:
            if counts[key] == 1:
                ordered_distincts.append(key)
        try:
            return ordered_distincts[k - 1]
        except:
            return ''

