# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        max_sum = 0
        node = head
        while(node):
            vals.append(node.val)
            node = node.next
        n = len(vals)
        for i in range(n//2):
            pair = [i, (n-1-i)]
            max_sum = max(max_sum, vals[i] + vals[n-1-i])

        return max_sum

