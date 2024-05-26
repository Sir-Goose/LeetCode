# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
    
        values = self.inorderTraversal(root)
        for value in values:
            if value >= low and value <= high:
                sum += value
        
        return sum

    def inorderTraversal(self, root): 
        if root is None:
            return []
       
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))  
        
        return result


