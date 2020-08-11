class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def search(root, key):
    if root.val == key or root is None:
        return True

    if key > root.val:
        return search(root.right, key)

    if key < root.val:
        return search(root.left, key)


def main():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.right.left = Node(13)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    if search(root, 4):
        print("--Yay! key found")
    else:
        print("--No key found")


if __name__ == '__main__':
    main()
