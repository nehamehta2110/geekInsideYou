"""
A node is a leaf node if both left and right child nodes of it are NULL.
For example, there are two leaves in following tree
        1
     /      \
   10      39
  /
5
"""


class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def countLeave(node):
    if node is None:
        return 0
    if node.left is None or node.right is None:
        return 1
    else:
        return countLeave(node.left) + countLeave(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Leaf count of the tree is %d" % (countLeave(root)))


if __name__ == '__main__':
    main()
