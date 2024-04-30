# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            next_node = cur.next
            prev.next = next_node
            cur.next = next_node.next
            next_node.next = cur
            prev = cur
            cur = cur.next
        return dummy.next
