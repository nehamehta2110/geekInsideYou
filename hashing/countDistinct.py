"""
Given an array of integers and a number K. \
Find the count of distinct elements in every window of size K in the array.
"""


def countDistinct(arr, N, K):
    # Code here

    res = []
    for i in range(N - k + 1):
        res.append(len(set(arr[i:i + k])))

    return res


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends
