class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        total_operations: List[int] = []

        for i in range(len(boxes)):
            operations = 0
            
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operations += abs(j - i)
            total_operations.append(operations)
        return total_operations
                
                

