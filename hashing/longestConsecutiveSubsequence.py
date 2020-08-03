"""
Given an array A of integers.
The task is to complete the function which returns an integer denoting the length of the
longest sub-sequence such that elements in the sub-sequence are consecutive integers,
the consecutive numbers can be in any order.
Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements
"""


# your task is to complete this function
# your function should return the length of the longest subsequence
def findLongestConsecutiveSubsequence(array, num):
    # code here

    s = set()
    ans = 0
    for element in array:
        s.add(element)

    for i in range(num):

        if array[i] - 1 not in s:
            j = array[i]
            while j in s:
                j += 1

            ans = max(ans, j - array[i])

    return ans


# {
#  Driver Code Starts
# Driver function
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        print(findLongestConsecutiveSubsequence(arr, n[0]))
# } Driver Code Ends
