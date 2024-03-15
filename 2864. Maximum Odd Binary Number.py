class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count: int = 0
        zero_count: int = 0
        
        for character in s:
            if character == '1':
                one_count += 1
            elif character == '0':
                zero_count += 1
        
        output: str = ''
        if one_count == 1:
            for i in range(len(s) - 1):
                output += '0'
            output += '1'
        
        else:
            output += '1'
            for i in range(one_count - 2):
                output += '1'
            for j in range(zero_count):
                output += '0'
            output += '1'
            

        return output
            
            
                
    
