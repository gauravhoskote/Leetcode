# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root, currmax, sol):
        if root == None:
            return
        
        if root.val >= currmax:
            sol[0] += 1
        
        self.f(root.left, max(currmax, root.val), sol)
        self.f(root.right, max(currmax, root.val), sol)

    def goodNodes(self, root: TreeNode) -> int:
        sol = [0]
        self.f(root, root.val, sol)
        return sol[0]
