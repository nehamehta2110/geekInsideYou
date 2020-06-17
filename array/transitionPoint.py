def transitionPoint(arr, n):
    """
    The task is to complete the function transitionPoint()
    that takes array and N as input and returns the value
    of the position where "0" ends and "1" begins.
    """
    for i in range(n):
        if arr[i] == 1:
            break
    if 1 not in arr:
        return -1
    return i


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
