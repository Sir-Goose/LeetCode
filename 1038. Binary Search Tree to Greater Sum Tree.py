# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # diy walk
        stack = [root]
        vals = []

        while stack:
            node = stack.pop()
            vals.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        stack = [root]

        while stack:
            node = stack.pop()
            value = node.val
            for val in vals:
                if val > value:
                    node.val += val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


