"""
program to find level order traversal of a tree
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printLevelOrder(root):
    h = heightOfTree(root)

    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value, end=" ")

    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def heightOfTree(node):
    if node is None:
        return 0
    else:
        left_height = heightOfTree(node.left)
        right_height = heightOfTree(node.right)
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
    print("The height of the tree is", (heightOfTree(root)))
    print("The level order traversal of the tree is")
    printLevelOrder(root)


if __name__ == '__main__':
    main()
