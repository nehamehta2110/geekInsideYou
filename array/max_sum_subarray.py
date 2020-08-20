def max_subarray(arr, n):
    """
    :param arr: given array
    :param n: size of array
    :return:
    """
    global_maximum = arr[0]
    current_maximum = arr[0]

    for i in range(1, n):
        current_maximum = max(arr[i], current_maximum + arr[i])
        global_maximum = max(current_maximum, global_maximum)

    return global_maximum


if __name__ == '__main__':
    T = int(input())
    for j in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print("maximum sub array sum:", max_subarray(arr, n))
