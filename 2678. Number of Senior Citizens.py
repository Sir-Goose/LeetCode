class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count: int = 0
        for human in details:
            print(human[11:13])
            if int(human[11:13]) > 60:
                count += 1 
        return count
        
