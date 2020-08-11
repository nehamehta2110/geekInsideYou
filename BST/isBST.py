"""
Given a binary tree. Check whether it is a BST or not.
Example 1:
Input:
    2
 /    \
1      3
Output: 1
"""
# User function Template for python3

from collections import deque


# return True if the given tree is a BST, else return False
def isBST(root):
    # code here
    def bstUtil(root, l=None, r=None):

        if root is None:
            return True

        if l is not None and l.data >= root.data:
            return False

        if r is not None and r.data <= root.data:
            return False

        return bstUtil(root.left, l, root) and bstUtil(root.right, root, r)

    return bstUtil(root, None, None)


# {
#  Driver Code Starts
# Initial Template for Python 3


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
    # string after splitting by space
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


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        if isBST(root):
            print(1)
        else:
            print(0)
# } Driver Code Ends
