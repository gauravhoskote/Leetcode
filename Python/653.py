# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def search(self, root, val, croot):
        if root == None:
            return False
        
        if val < root.val:
            return self.search(root.left, val, croot)
        elif val > root.val:
            return self.search(root.right, val, croot)
        else:
            return True and (root != croot)

    def traverse(self, croot, val, root, sol):
        if croot == None:
            return
        
        sol[0] = sol[0] or self.search(root, val - croot.val, croot)

        self.traverse(croot.left, val, root, sol)
        self.traverse(croot.right, val, root, sol)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sol = [False]
        self.traverse(root,k,root,sol)
        return sol[0]
