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

        sol[0] = sol[0] and (abs(right - left) <= 1)
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        sol = [True]
        self.f(root, sol)
        return sol[0]
