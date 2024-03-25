# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        dq = deque()
        dq.append(root)
        if root == None:
            return sol
        while dq:
            x = len(dq)
            sol.append([])
            while x:
                node = dq.popleft()
                sol[-1].append(node.val)
                x -= 1
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return sol
