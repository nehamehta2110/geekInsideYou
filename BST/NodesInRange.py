# User function Template for python3
"""
Count BST nodes that lie in a given range
Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.
The values smaller than root go to the left side
The values greater and equal to the root go to the right side
"""


def getCountOfNode(root, l, h):
    if root is None:
        return 0

    if root.data == h and root.data == l:
        return 1

    if h >= root.data >= l:
        return (1 + getCountOfNode(root.left, l, h) +
                getCountOfNode(root.right, l, h))


    elif root.data < l:
        return getCountOfNode(root.right, l, h)

    else:
        return getCountOfNode(root.left, l, h)

    # {


#  Driver Code Starts
# Initial Template for Python 3

# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp = Node()
    temp.data = value
    temp.left = None
    temp.right = None
    return temp


def newNode(root, data):
    if root is None:
        root = createNewNode(data)
    elif data < root.data:
        root.left = newNode(root.left, data)
    else:
        root.right = newNode(root.right, data)

    return root


def main():
    testcases = int(input())
    while testcases > 0:
        root = None
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]
        for i in arr:
            root = newNode(root, i)

        lr = [int(x) for x in input().strip().split()]

        print(getCountOfNode(root, lr[0], lr[1]))
        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
