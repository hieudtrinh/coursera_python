import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(argv, arc):
    print(argv, arc)
    node = TreeNode(10)
    print(node.val)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
