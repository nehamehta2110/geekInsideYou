"""
Ceil in BST
Given a BST and a number X. The task it to find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.
"""
import atexit
import io
import sys


# User function Template for python3
# Function to find ceil of a given input in BST. If inp
# is more than the max key in BST, return -1
def findCeil(root, inp):
    # code here

    if root is None:
        return -1

    if root.key == inp:
        return root.key

    if root.key < inp:
        return findCeil(root.right, inp)

    fc = findCeil(root.left, inp)

    return fc if fc >= inp else root.key


# {
#  Driver Code Starts
# Initial Template for Python 3

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class:
class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


# Tree Class
class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x:  # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:  # go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return  # no duplicate is to be inserted

        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)
        return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        x = int(input())
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        print(findCeil(tree.root, x))

# } Driver Code Ends
