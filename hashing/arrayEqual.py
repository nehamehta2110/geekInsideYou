"""
Check if two arrays are equal or not
Given two given arrays of equal length, the task is to find if given arrays are equal or not.
Two arrays are said to be equal if both of them contain same set of elements,
arrangements (or permutation) of elements may be different though.
Input  : arr1[] = {1, 2, 5, 4, 0};
         arr2[] = {2, 4, 5, 0, 1};
Output : Yes
"""


# User function Template for python3

def check(arr1, arr2, n):
    # return: True or False

    # code here
    hs = {}

    if len(arr1) != len(arr2):
        return False

    for i in range(n):
        if arr1[i] in hs:
            hs[arr1[i]] += 1
        else:
            hs[arr1[i]] = 1

    for i in range(n):
        if arr2[i] not in hs.keys():
            return False

        if hs[arr2[i]] == 0:
            return False

        hs[arr2[i]] -= 1

    return True


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for tc in range(t):

        n = int(input())

        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        if check(arr1, arr2, n):
            print(1)
        else:
            print(0)

# } Driver Code Ends
