# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_string = ''
        node = head
        while(node):
            binary_string += str(node.val)
            node = node.next
        return int(binary_string, 2)

