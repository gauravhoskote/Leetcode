# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def f(self, sol, root):
        if root == None:
            return 0, max(sol, 0)
        leftres = self.f(sol, root.left)
        rightres = self.f(sol, root.right)
        sol = max(sol, leftres[0] + rightres[0])
        
        return 1 + max(leftres[0],  rightres[0]), sol

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, sol = self.f(-1, root)
        return sol
