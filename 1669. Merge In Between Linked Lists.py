# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodes = []
        node = list1
        while(node):
            nodes.append(node.val)
            node = node.next
        
        root = ListNode(nodes[0])
        node = root
        for i in range(1, len(nodes)):
            if i == a:
                noode = list2
                while(noode):
                    node.next = noode
                    noode = noode.next
                    node = node.next
            elif i > a and i <= b:
                pass
            else:
                node.next = ListNode(nodes[i])
            print(node)
            if node.next is not None:
                node = node.next
        
        return root
             
        
