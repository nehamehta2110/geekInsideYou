# User function Template for python3
"""
Given a Two Binary Trees, write a function that returns true if one is mirror of other,
else returns false.
Input:
2
1 2 3
1 3 2
10 20 30 40 60
10 20 30 40 60
Output:
1
0
"""

from collections import deque

"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


def areMirror(root1, root2):
    """
    :param root1: root of the given tree 1
    :param root1: root of the given tree 2
    :return: True False
    """
    # code here
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return areMirror(root1.left, root2.right) and areMirror(root1.right, root2.left)
    return False


# {
#  Driver Code Starts


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        str1 = input()
        str2 = input()
        root1 = buildTree(str1)
        root2 = buildTree(str2)
        if areMirror(root1, root2):
            print(1)
        else:
            print(0)

# } Driver Code Ends
