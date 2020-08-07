"""
Given a Binary Tree and a Key.
The task is to insert the key into the binary tree at first position available in level order.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(node.key, end=" ")
        inorderTraversal(node.right)


def insertion(node, element):
    q = []
    q.append(node)
    while len(q):
        node = q[0]
        q.pop(0)
        if not node.left:
            node.left = Node(element)
            break
        else:
            q.append(node.left)

        if not node.right:
            node.right = Node(element)
            break
        else:
            q.append(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("The inorder order traversal of the tree is")
    inorderTraversal(root)
    print()
    insertion(root, 12)
    print("The inorder order traversal of the tree is")
    inorderTraversal(root)


if __name__ == '__main__':
    main()
