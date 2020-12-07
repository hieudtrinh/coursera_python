from unittest import TestCase

from MergeTwoBinaryTrees import MergeTwoBinaryTrees
from TreeNode import TreeNode


class TestMergeTwoBinaryTrees(TestCase):
    def test_merge_trees(self):
        self.solution = MergeTwoBinaryTrees()
        n5 = TreeNode(5)
        n3 = TreeNode(3, n5, None)
        n2 = TreeNode(2)
        n1 = TreeNode(1, n3, n2)

        m4 = TreeNode(4)
        m1 = TreeNode(1, None, m4)
        m7 = TreeNode(7)
        m3 = TreeNode(3, None, m7)
        m2 = TreeNode(2, m1, m3)

        root = self.solution.mergeTrees(n1, m2)
        self.printTreeNode(root)

    def printTreeNode(self, n: TreeNode):
        if n is None: return
        print(n.val)
        self.printTreeNode(n.left)
        self.printTreeNode(n.right)
