# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = self.maxDepth(root)
        print(max_depth)
        values = self.nodes_at_max_depth(root, max_depth)
        print(values)

        
        return sum(values)

    
    
    def maxDepth(self, root):
        if root is None:
            return 0
    
        stack = [(root, 1)]
        max_depth = 0
    
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
        
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
    
        return max_depth

    def nodes_at_max_depth(self, root, maxDepth):
        if root is None:
            return 0
    
        stack = [(root, 1)]
        max_depth = 0
        max_values = []
    
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if depth == maxDepth:
                max_values.append(node.val)
        
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_values
    

        
