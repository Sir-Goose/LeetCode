# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        running_total = 0
        curr = head
        while(curr):
            if curr.val == 0:
                if running_total > 0:
                    vals.append(running_total)
                    running_total = 0
            else:
                running_total += curr.val

            curr = curr.next
        print(vals)   
        
        # make new list

        head = ListNode(vals[0])
        curr = head
        for i in range(1, len(vals)):
            curr.next = ListNode(vals[i])
            curr = curr.next
        return head





