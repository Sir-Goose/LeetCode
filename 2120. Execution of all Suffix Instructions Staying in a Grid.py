class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        output = [] 
        # in bounds if both cords < n and both cords >= 0
        
        pos_row = 0
        pos_col = 0
        
        for i in range(len(s)):
            subset = s[i:]
            pos_row = startPos[0]
            pos_col = startPos[1]
            #print(f"i: {i}")
            #print(subset)
            for j in range(len(subset)):
                #print(f"j: {j}")
                if subset[j] == 'L':
                    pos_col -= 1
                if subset[j] == 'R':
                    pos_col += 1 
                if subset[j] == 'U':
                    pos_row -= 1
                if subset[j] == 'D':
                    pos_row += 1
                
                if pos_row >= n or pos_row < 0:
                    output.append(j)
                    #print('Row Break')
                    break
                    
                elif pos_col >= n or pos_col < 0:
                    output.append(j)
                    #print("Col Break")
                    break
                    
                if j == len(subset) - 1:
                    output.append(j+1)
                    
           
        return output
                
