# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        dq = deque()
        dq.append(root)
        if root == None:
            return sol
        while dq:
            node = dq.popleft()
            offset = 0
            if node.right:
                dq.append(node.right)
                offset += 1
            if node.left:
                dq.append(node.left)
                offset += 1
            sol.append(node.val)
            x = len(dq) - offset
            while x:
                x -= 1
                node = dq.popleft()
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
        return sol
