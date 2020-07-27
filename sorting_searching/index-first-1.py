"""
Find the index of first 1 in a sorted array of 0’s and 1’s
Description - We are given an sorted boolean array, We have to find out the index of first 1 in the Array
Input : arr[] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
Output : 6
The index of first 1 in the array is 6.
Solution - One simple solution can be traverse the Array and find out the first index of 1. Since the array is sorted,
we can optimize the solution using binary search by reducing the effective search space in each step.
"""


def find_index_one(arr, l, r):
    if l <= r:
        m = l + (r - l) // 2
        if (arr[m] == 1) and (m == 0 or arr[m - 1] == 0):
            return m
        elif arr[m] == 1:
            return find_index_one(arr, l, m - 1)
        else:
            return find_index_one(arr, m + 1, r)


print(find_index_one(arr=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1], l=0, r=9))
