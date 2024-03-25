# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, l, r):
        if root == None:
            return True
        if root.val > l and root.val < r:
            return self.f(root.left, l, root.val) and self.f(root.right, root.val, r)
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.f(root, float('-inf'), float('inf'))
