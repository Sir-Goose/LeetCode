class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        sizes = {}

        for size in groupSizes:
            if size in sizes:
                sizes[size] = sizes[size] + 1
            else:
                sizes[size] = 1
        
        for key in sizes:
            sizes[key] = int(sizes[key]) / int(key) 


        for key in sizes:
            for i in range(int(sizes[key])):
                groups.append([-1]*key)
        print(sizes)
        print(groups)

        for i in range(len(groupSizes)):
            for j in range(len(groups)):
                if len(groups[j]) == groupSizes[i] and -1 in groups[j]:
                    groups[j].append(i)
                    groups[j] = groups[j][1:]
                    break
        print(groups)

        return groups

