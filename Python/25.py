# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def f(self, curr, ctr, q):
        if curr == None:
            return
        if ctr == 1:
            q.append(curr.val)
            curr.val = q[0]
            q.popleft()
        else:
            q.append(curr.val)
            self.f(curr.next, ctr-1, q)
            curr.val = q[0]
            q.popleft()

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = deque()
        t = head
        while t:
            ctr = k
            curr = t
            b = t
            print(b.val)
            while b and ctr:
                b = b.next
                ctr-=1
            if ctr:
                break
            ctr = k
            self.f(curr, ctr, q)
            ctr = k
            while t and ctr:
                t = t.next
                ctr-=1
        return head
