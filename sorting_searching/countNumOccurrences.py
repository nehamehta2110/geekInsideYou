"""
Count number of Occurences in Sorted Array
Description - Given a sorted array arr[ ] and a number x, We have to count the occurrences of x in arr[ ].
Input : [1, 1, 2, 2, 2, 2, 3] , x = 2
Output : 4
"""


def first_index(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first_index(arr, (mid + 1), high, x, n)
        else:
            return first_index(arr, low, (mid - 1), x, n)


def last_index(arr, low, high, x, n):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last_index(arr, low, (mid - 1), x, n)
        else:
            return last_index(arr, (mid + 1), high, x, n)


def count_occurrences(arr, n, x):
    i = first_index(arr, 0, n - 1, x, n)
    j = last_index(arr, 0, n - 1, x, n)
    count = j - i + 1
    return count


arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
print(count_occurrences(arr, len(arr), x))
