from unittest import TestCase
from IncreasingOrderSearchTree import IncreasingOrderSearchTree
from TreeNode import TreeNode


class TestIncreasingOrderSearchTree(TestCase):
    def test_inorder(self):
        self.solution = IncreasingOrderSearchTree()
        n1 = TreeNode(1)
        n2 = TreeNode(2, n1, None)
        n4 = TreeNode(4)
        n3 = TreeNode(3, n2, n4)
        n7 = TreeNode(7)
        n9 = TreeNode(9)
        n8 = TreeNode(8, n7, n9)
        n6 = TreeNode(6, None, n8)
        n5 = TreeNode(5, n3, n6)
        root = self.solution.increasingBST(n5)

        while root is not None:
            print(root.val)
            root = root.right
