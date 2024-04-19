# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_sum(self, root, low, high , sol):
        if root == None:
            return
        if root.val <= high and root.val >= low:
            sol[0] = sol[0] + root.val
        self.get_sum(root.left, low, high, sol)
        self.get_sum(root.right, low, high, sol)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sol = [0]
        self.get_sum(root, low, high, sol)
        return sol[0]
