from TreeNode import TreeNode


class IncreasingOrderSearchTree:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.current = dummy = TreeNode()
        self.inorder(root)
        return dummy.right

    def inorder(self, root: TreeNode):
        if root is None:
            return root
        self.inorder(root.left)
        root.left = None
        self.current.right = root
        self.current = self.current.right
        self.inorder(root.right)
