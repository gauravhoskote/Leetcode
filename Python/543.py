# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, sol):
        if root == None:
            return 0
        left = self.f(root.left, sol)
        right = self.f(root.right, sol)
        sol[0] = max(sol[0], 1 + left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = []
        sol.append(0)
        self.f(root, sol)
        return sol[0]-1
