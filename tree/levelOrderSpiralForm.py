"""
Write a function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.
spiral_order
"""


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def spiralOrder(root):
    h = heightOfTree(root)
    ltr = False

    for i in range(1, h + 1):
        spiralPrintLevel(root, i, ltr)
        ltr = not ltr


def spiralPrintLevel(root, level, ltr):
    if root is None:
        return

    if level == 1:
        print(root.val, end=" ")

    if level > 1:

        if ltr:

            spiralPrintLevel(root.left, level - 1, ltr)
            spiralPrintLevel(root.right, level - 1, ltr)

        else:
            spiralPrintLevel(root.right, level - 1, ltr)
            spiralPrintLevel(root.left, level - 1, ltr)


def heightOfTree(node):
    if node is None:
        return 0

    else:

        l_height = heightOfTree(node.left)
        r_height = heightOfTree(node.right)

        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print("--The spiral order traversal of the tree is")
    spiralOrder(root)


if __name__ == '__main__':
    main()
