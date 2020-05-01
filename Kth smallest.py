def kthsmallestNumber(arr, n, k):
    arr.sort()
    return arr[k - 1]


if __name__ == '__main__':
    arr = [2, 35, 16, 78, 4, 31, 167]
    n = len(arr)
    k = 3
    if k < n:
        print("The {}th smallest number is {}".format(k, kthsmallestNumber(arr, n, k)))
