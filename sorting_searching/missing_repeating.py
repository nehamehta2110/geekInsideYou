"""
given arr[2,3,2,1,5] output repeating number 2 and missing number 4
negative indexing method:
arr[abs(arr[index])-1]
"""


def repeat_and_miss(arr, size):
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print("--Repeating element is", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("--Missing element is", i + 1)


arr = [2, 3, 2, 1, 5]
n = len(arr)
repeat_and_miss(arr, n)
