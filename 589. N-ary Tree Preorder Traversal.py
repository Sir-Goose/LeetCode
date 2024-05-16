"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        vals = []
        stack = [root]

        while stack:
            node = stack.pop()
            vals.append(node.val)

            if node.children:
                stack.extend(reversed(node.children))
        
        return vals

