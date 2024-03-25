"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        t = head
        if head == None:
            return None
        while t:
            mp[t] = Node(t.val)
            t = t.next
        for k,v in mp.items():
            if k.next:
                v.next = mp[k.next]
            if k.random:
                v.random = mp[k.random]
        return mp[head]
