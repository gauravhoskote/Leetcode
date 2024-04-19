# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, arr, flag):
        if root == None:
            return
        
        if root.left == None and root.right == None and flag:
            arr.append(root.val)
        
        self.f(root.left, arr, True)
        self.f(root.right, arr, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.f(root, arr, False)
        return sum(arr)
