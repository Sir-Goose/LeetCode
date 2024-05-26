class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output = []
        i = 0
        remaining_nums = nums
        while True:
            temp = []
            for number in remaining_nums:
                try:
                    x = output[i]
                except:
                    output.append([])
                if number not in output[i]:
                    output[i].append(number)
                else:
                    temp.append(number)
            remaining_nums = temp
            i += 1
            if temp == []:
                break

        return output 
                    
                
