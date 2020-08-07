"""
program to find height of a binary tree using recursive method
"""


class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def maxHeight(node):
    if node is None:
        return 0
    else:
        left_height = maxHeight(node.left)
        right_height = maxHeight(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("The height of the tree is", (maxHeight(root)))


if __name__ == '__main__':
    main()
