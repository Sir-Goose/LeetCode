# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        curr = head
        top = head
        mid_values = []
        val1 = None
        val2 = None


        while curr != None:
            if val1 == None:
                val1 = curr.val
                nnode = curr.next
                if nnode != None:
                    val2 = nnode.val


            if val1 != None and val2 != None:
                mid_values.append(math.gcd(val1, val2))
                val1 = None
                val2 = None
            curr = curr.next
        
        print(mid_values)

        curr = head
        i = 0
        while curr != None:
            print(i)
            if i == len(mid_values):
                break

            new_node = ListNode(mid_values[i])
            next_node = curr.next
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
            i += 1
        return head 
