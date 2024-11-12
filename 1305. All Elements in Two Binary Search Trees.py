# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        tree1 = self.inorder_iterative(root1)
        tree2 = self.inorder_iterative(root2)
        combined = []
        for element in tree1:
            combined.append(element)
        for element in tree2:
            combined.append(element)
        return sorted(combined)


    def inorder_iterative(self, root):
        elements = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            elements.append(current.val)
            current = current.right
        return elements
