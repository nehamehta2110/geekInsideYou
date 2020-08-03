"""
Given an array of positive integers and an integer.
Determine whether or not there exist two elements in A whose sum is exactly equal to that integer.
"""


# User function Template for python3

# A[] : the input array of positive integers
# N : size of the array arr[]
# X : the required sum
def keypair(A, N, X):
    # code here

    for i in range(N):
        X1 = X - A[i]
        A[i] = 0

        if X1 > 0 and X1 in A:
            return True
    return False


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    t = int(input())
    for _ in range(0, t):
        n, x = list(map(int, input().split()))
        a = list(map(int, input().split()))
        sln = keypair(a, n, x)
        if sln:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
# } Driver Code Ends
