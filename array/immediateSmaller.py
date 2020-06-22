def immediateSmaller(arr, n, x):
    """
    Given an array arr[] of size N containing positive integers
    and an integer X. You need to find the value in the array
    which is smaller than X and closest to it. You will be given a function
    immediateSmaller() whose signature description given below:
    """
    # code here
    arr2 = []
    for i in range(n):
        if arr[i] < x:
            arr2.append(arr[i])
        i += 1
    n1 = len(arr2)
    if not arr2:
        return -1
    else:
        for j in range(n1 - 1):
            for k in range(n1 - j - 1):
                if arr2[k] > arr2[k + 1]:
                    arr2[k], arr2[k + 1] = arr2[k + 1], arr2[k]
        return arr2[-1]


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(e) for e in input().split()]
        x = int(input())

        ans = immediateSmaller(arr, n, x)
        print(ans)
