class Node:
    def __init__(self, value):
        """
        Initialisation of node, pointer to left child and
        pointer to right child
        """
        self.value = value
        self.right = None
        self.left = None


def main():
    """
    driver function
    """
    rootNode = Node(1)
    rootNode.left = Node(2)
    rootNode.right = Node(3)
    rootNode.left.left = Node(4)
    rootNode.left.right = Node(5)


if __name__ == '__main__':
    main()
