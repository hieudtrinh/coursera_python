from unittest import TestCase
from SearchInBinarySearchTree import SearchInBinarySearchTree
from TreeNode import TreeNode


class Test(TestCase):
    def test_search_in_binary_search_tree(self):
        self.solution = SearchInBinarySearchTree()
        n1 = TreeNode(1)
        n3 = TreeNode(3)
        n2 = TreeNode(2, n1, n3)
        n7 = TreeNode(7)
        n4 = TreeNode(4, n2, n7)
        node: TreeNode = self.solution.searchBST(n4, 2)
        self.assertIsNotNone(node)
