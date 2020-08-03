"""
Max distance between same elements
Given an array with repeated elements,
the task is to find the maximum distance between two occurrences of an element.
Input : arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
Output: 10
// maximum distance for 2 is 11-1 = 10
// maximum distance for 1 is 4-2 = 2
// maximum distance for 4 is 10-5 = 5
"""


# Your task is to Complete this function
# function should return an integer
def maxDistance(A, num):
    # Code here

    hs = {}

    counter = 0

    for i in range(num):

        if A[i] not in hs.keys():
            hs[A[i]] = i

        else:

            counter = max(counter, i - hs[A[i]])

    return counter


# {
#  Driver Code Starts
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        print(maxDistance(A, n))


if __name__ == '__main__':
    main()

# } Driver Code Ends
