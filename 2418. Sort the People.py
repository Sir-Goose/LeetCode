class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = []

        for i in range(len(names)):
            tuples.append([names[i], heights[i]])

        print(tuples)


        
        tuples = sorted(tuples, key=lambda item: item[1], reverse=True)

        print(tuples)

        sorted_names = []

        for i in range(len(tuples)):
            sorted_names.append(tuples[i][0])
        
        return sorted_names
