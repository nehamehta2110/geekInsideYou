"""
Algo:
* if x matches mid1, return mid1
* else if x matches mid2, return mid2
* else if x is less than mid1, x will be in first part
* else if x is greater than mid2, x will be in third part
* else if x will be in second part
"""


def ter_search(A, left, right, k):
    # Code here
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if A[mid1] == k:
            return mid1
        elif A[mid2] == k:
            return mid2
        elif A[mid1] > k:
            return ter_search(A, left, mid1 - 1, k)
        elif A[mid2] < k:
            return ter_search(A, mid2 + 1, right, k)
        else:
            return ter_search(A, mid1 + 1, mid2 - 1, k)
    return -1


# {
#  Driver Code Starts
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input())
    print(ter_search(arr, 0, n - 1, x))
# } Driver Code Ends
