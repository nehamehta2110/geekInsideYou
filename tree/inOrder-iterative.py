class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrder(root):
    current = root
    stack = []

    while True:

        if current is not None:
            stack.append(current)
            current = current.left

        elif stack:
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right

        else:
            break


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("--The inorder traversal of the tree is")
    inOrder(root)


if __name__ == '__main__':
    main()
