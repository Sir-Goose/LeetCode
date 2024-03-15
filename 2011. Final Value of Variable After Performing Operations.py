class Solution:

    x: int = 0

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        for operation in operations:
            self.apply_operation(operation)
        
        return self.x

    def apply_operation(self, operation: int) -> int:
        if operation == "++X" or operation == "X++":
            self.x += 1
        elif operation == "--X" or operation == "X--":
            self.x -= 1

