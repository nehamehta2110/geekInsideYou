"""
You are given an array of integers. You need to print the non-repeated elements as
they appear in the array.
Example 1:
Input: n = 10 arr[] = {1,1,2,2,3,3,4,5,6,7}
Output: 4 5 6 7
Explanation: 4, 5, 6 and 7 are the only elements which is having only 1 frequency and hence, Non-repeating.
"""


# User function Template for python3

# Complete this function
def printNonRepeated(arr, n):
    # Your code here

    hs = {}
    ans = []

    for i in range(n):
        if arr[i] in hs.keys():
            hs[arr[i]] += 1
        else:
            hs[arr[i]] = 1

    for i in range(n):
        if hs[arr[i]] == 1:
            ans.append(arr[i])

    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        l = printNonRepeated(arr, n)
        print(*l)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
