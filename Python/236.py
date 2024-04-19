# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def get_lca(self, root, p, q, sol):
        if root == None:
            return False
        
        res_left = self.get_lca(root.left, p, q, sol)
        res_right = self.get_lca(root.right, p, q, sol)
        if res_left and res_right:
            sol[0] = root
            return True
        
        if res_left or res_right:
            if root.val == p.val or root.val == q.val:
                sol[0] = root
            return True
        
        if root.val == p.val or root.val == q.val:
            return True
        return False


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol = [None]
        _ = self.get_lca(root, p, q, sol)
        return sol[0]
