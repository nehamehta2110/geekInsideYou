"""
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours.
For corner elements, we need to consider only one neighbour.
"""


def peak_element(arr, l, r, n):
    mid = l + (r - l) // 2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) & (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif mid > 0 & arr[mid] < arr[mid - 1]:
        return peak_element(arr, l, mid - 1, n)
    else:
        return peak_element(arr, mid + 1, r, n)


print(peak_element(arr=[10, 20, 15, 2, 23, 90, 6], l=0, r=6, n=7))
