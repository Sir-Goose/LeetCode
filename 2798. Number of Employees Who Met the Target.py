class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output = 0
        for employee in hours:
            if employee >= target:
                output += 1

        return output
        
