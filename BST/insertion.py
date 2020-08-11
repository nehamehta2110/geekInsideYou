class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        root = key

    else:
        if root.val < key.val:
            if root.right is None:
                root.right = key
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = key
            else:
                insert(root.left, key)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)


def main():
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))
    inorder(r)
    print()
    insert(r, Node(5))
    inorder(r)


if __name__ == '__main__':
    main()
