class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            length = len(students)

            for i in range(len(students)):

                if students[0] == sandwiches[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    students.append(students.pop(0))
            if len(students) == length:
                break
        
        return len(sandwiches)

                
