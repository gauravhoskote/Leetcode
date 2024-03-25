# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t = head
        cnt = 0
        while t.next:
            t = t.next
            cnt += 1
        mid = cnt //2
        t = head
        while mid:
            t = t.next
            mid -= 1
        prev = None
        curr = t
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        r = prev
        l = head
        while l:
            t = l.next
            l.next = r
            t2 = r.next
            r.next = t
            l = t
            r = t2
        return head
