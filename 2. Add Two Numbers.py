# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_digits = []
        l2_digits = []

        while l1:
            l1_digits.append(l1.val)
            l1 = l1.next

        while l2:
            l2_digits.append(l2.val)
            l2 = l2.next

        l1_digits.reverse()
        l2_digits.reverse()

        num1 = ''.join(str(digit) for digit in l1_digits)
        num2 = ''.join(str(digit) for digit in l2_digits)
        sum = int(num1) + int(num2)

        sum_digits = []
        for digit in str(sum):
            sum_digits.append(digit)
        sum_digits.reverse()


        dummy_head = ListNode(0)
        current = dummy_head

        for val in sum_digits:
            current.next = ListNode(int(val))
            current = current.next

        return dummy_head.next
