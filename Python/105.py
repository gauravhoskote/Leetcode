class Solution:

    def build(self, root, pre, ino):
        if ino:
            root = TreeNode(pre[0])
            mid = ino.index(pre[0])
            pre.pop(0)
            root.left = self.build(root.left, pre, ino[:mid])
            root.right = self.build(root.right, pre, ino[mid+1:])
            return root
        else:
            return None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        return self.build(root, preorder, inorder)
