# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode
        d.next = head
        th = d
        while n:
            n -= 1
            th = th.next
        prev = d
        while th.next:
            prev = prev.next
            th = th.next
        prev.next = prev.next.next
        return d.next
