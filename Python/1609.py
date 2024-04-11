# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        dq = collections.deque()
        dq.append(root)
        ctr = 0
        while dq:
            l = len(dq)
            if ctr == 0:
                prev = float('-inf')
            else:
                prev = float('inf')
            for i in range(l):
                x = dq.popleft()
                if ctr == 0:
                    if x.val <= prev or x.val%2 == 0:
                        return False
                    if x.left is not None:
                        dq.append(x.left)
                    if x.right is not None:
                        dq.append(x.right)
                else:
                    if x.val >= prev or x.val%2 == 1:
                        return False
                    if x.left is not None:
                        dq.append(x.left)
                    if x.right is not None:
                        dq.append(x.right)
                prev = x.val
            ctr = ((ctr+1)%2)
        return True
