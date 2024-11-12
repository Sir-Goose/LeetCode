class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = []
        groups = []
        output = []
        for num in set(nums):
            frequency.append([num, 0])
        for num in nums:
            for i in range(len(frequency)):
                if frequency[i][0] == num:
                    frequency[i][1] += 1
        print(frequency)
        frequency = sorted(frequency, key=lambda x: x[1])
        print(frequency)
        #for i in range(len(sorted_list))
        swapped = True
        while swapped == True:
            swapped = False
            for i in range(len(frequency)-1):
                if frequency[i][1] == frequency[i+1][1]:
                    if frequency[i][0] < frequency[i+1][0]:
                        swapped = True
                        temp = frequency[i+1][0]
                        frequency[i+1][0] = frequency[i][0]
                        frequency[i][0] = temp
        print(frequency)
        for pair in frequency:
            group = [pair[0]] * pair[1]
            groups.append(group)

        for group in groups:
            for item in group:
                output.append(item)
        return output
