class Solution:

    def f(self, root, sol):
        if root == None:
            return 0
        
        lsum = self.f(root.left, sol)
        rsum = self.f(root.right, sol)

        sol[0] = max(sol[0], root.val + lsum + rsum,root.val + lsum, root.val + rsum, root.val)
        return max(root.val + max(lsum , rsum), root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = [float('-inf')]
        _ = self.f(root, sol)
        return sol[0]
