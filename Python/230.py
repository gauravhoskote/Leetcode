# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root, sol, k, node):
        if root == None:
            return
        left = self.f(root.left, sol, k, node)
        sol[0]+=1
        if sol[0] == k:
            node[0] = root.val
        right = self.f(root.right, sol, k, node)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = [-1]
        sol = [0]
        self.f(root, sol, k, node)
        return node[0]
