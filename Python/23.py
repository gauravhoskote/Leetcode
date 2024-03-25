# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        hq = []
        heapq.heapify(hq)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hq, (lists[i].val, i))
        head = ListNode()
        t = head
        while len(hq):
            x = heapq.heappop(hq)
            t.next = ListNode(x[0])
            # print(x[1])
            i = x[1]
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(hq, (lists[i].val, i))
            t = t.next
        
        return head.next
