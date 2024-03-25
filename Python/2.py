# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        reshead = ListNode()
        t = reshead
        while l1 or l2 or carry:
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            res += carry
            t.val = res % 10
            if res > 9:
                carry = 1
            else:
                carry = 0
            if l1 or l2 or carry:
                t.next = ListNode()
                t = t.next
        return reshead
