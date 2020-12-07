from TreeNode import TreeNode


class MergeTwoBinaryTrees:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        if not t1 or not t2:
            return t1 if t1 else t2
        return TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left),
                        self.mergeTrees(t1.right, t2.right))
