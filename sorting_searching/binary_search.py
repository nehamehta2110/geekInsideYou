"""
Algo:
* if x matches middle element, return middle index
* else if x is less than mid, x will be in left half
* else if x is greater than mid, x will be in right half
"""


def bin_search(A, left, right, k):
    # Code here
    if right >= left:
        mid = left + (right - left) // 2
        if A[mid] == k:
            return mid
        elif A[mid] < k:
            return bin_search(A, mid + 1, right, k)
        elif A[mid] > k:
            return bin_search(A, left, mid - 1, k)
    return -1


# {
#  Driver Code Starts
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input())
    print(bin_search(arr, 0, n - 1, x))
# } Driver Code Ends
