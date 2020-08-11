"""
Write a function that returns true if the given Binary Tree of size N is SumTree else return
false. A SumTree is a Binary Tree in which value of each node x is equal to sum of nodes present in its left subtree and right subtree . An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Following is an example of SumTree.
          26
        /    \
      10      3
    /   \   /   \
   4     6  1    2
"""
from collections import deque


# your task is to complete this function
# function should return True is Tree is SumTree else return False
def sum(node):
    if node is None:
        return 0

    return sum(node.left) + node.data + sum(node.right)


def isSumTree(root_node):
    # Code here

    if root_node is None or (root_node.left is None and root_node.right is None):
        return True

    lr = sum(root_node.left)
    rr = sum(root_node.right)

    if root_node.data == lr + rr and isSumTree(root_node.left) and isSumTree(root_node.right):
        return True
    return False


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
        if isSumTree(root):
            print(1)
        else:
            print(0)
# } Driver Code Ends
