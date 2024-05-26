# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        
        head = ListNode(vals.pop())
        node = head
        while len(vals) > 0:
            node.next = ListNode(vals.pop())
            node = node.next
        
        return head

