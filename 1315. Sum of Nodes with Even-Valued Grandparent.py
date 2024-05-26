# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # walk the tree
        nodes = []
        grandkids = []
        total = 0

        stack = [root]
        while(stack):
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if node.val % 2 == 0:
                #check the grandkids
                if node.left:
                    child1 = node.left
                    if child1.left:
                        grandkids.append(child1.left)
                    if child1.right:
                        grandkids.append(child1.right)

                if node.right:
                    child2 = node.right
                    if child2.left:
                        grandkids.append(child2.left)
                    if child2.right:
                        grandkids.append(child2.right)

        for grandkid in grandkids:
            total += grandkid.val

        return total

                
                


