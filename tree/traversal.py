class Node:
    def __init__(self, value):
        """
        Initialisation of node, pointer to left child and
        pointer to right child
        """
        self.value = value
        self.right = None
        self.left = None


def inOrder(root):
    """
    InOrder traversal, traverse left child, traverse root node, traverse right child
    """
    if root:
        inOrder(root.left)
        print(root.value)
        inOrder(root.right)


def preOrder(root):
    """
    PreOrder traversal, traverse root node, traverse left child, traverse right child
    """
    if root:
        print(root.value)
        inOrder(root.left)
        inOrder(root.right)


def postOrder(root):
    """
    PostOrder traversal, traverse left child,traverse right child, traverse root node
    """
    if root:
        inOrder(root.left)
        inOrder(root.right)
        print(root.value)


def main():
    """
    driver function
    """
    rootNode = Node(1)
    rootNode.left = Node(2)
    rootNode.right = Node(3)
    rootNode.left.left = Node(4)
    rootNode.left.right = Node(5)
    print("--InOrder")
    inOrder(rootNode)
    print("--PreOrder")
    preOrder(rootNode)
    print("--PostOrder")
    postOrder(rootNode)


if __name__ == '__main__':
    main()
