"""
The first line of the input contains an integer 'T' denoting the number of test cases.
Then T test cases follow. First line of each test case contains an integer Q denoting the number of queries .
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)
The second line of each test case contains Q queries separated by space.
"""


def Push(x, stack1, stack2):
    """
    x: value to push
    stack1: list
    stack2: list
    """
    while len(stack1) != 0:
        stack2.append(stack1[-1])
        stack1.pop()

    # Push item into self.s1
    stack1.append(x)

    # Push everything back to s1
    while len(stack2) != 0:
        stack1.append(stack2[-1])
        stack2.pop()

    # code here


def Pop(stack1, stack2):
    """
    stack1: list
    stack2: list
    """

    # code here
    if len(stack1) == 0:
        return -1

    # return the last element and pop it
    x = stack1[-1]
    stack1.pop()
    return x


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                Push(qtyp_qry[i + 1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(Pop(stack1, stack2), end=' ')
                i += 1

        print()
# } Driver Code Ends
