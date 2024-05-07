# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        def build_tree(vals, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(vals[mid])
            node.left = build_tree(vals, start, mid - 1)
            node.right = build_tree(vals, mid + 1, end)
            return node

        vals = inorder(root)
        vals.sort()
        return build_tree(vals, 0, len(vals) - 1)

