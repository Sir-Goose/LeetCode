# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # for each node need to just walk all the nodes beneath it and average that. 
        count = 0

        nodes = self.get_all_nodes(root)

        for node in nodes:
            values = self.get_all_values(node)
            print(f"Average: {sum(values) / len(values)}")
            if node.val == math.floor(sum(values) / len(values)):
                count += 1
        
        return count





    def get_all_nodes(self, root):
        if not root:
            return []
    
        nodes = []
        stack = [root]
    
        while stack:
            node = stack.pop()
            nodes.append(node)
        
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
        return nodes

    def get_all_values(self, root):
        if not root:
            return []
    
        values = []
        stack = [root]
    
        while stack:
            node = stack.pop()
            values.append(node.val)
        
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
        return values
