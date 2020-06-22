# User function Template for python3
def firstRepeated(arr, n):
    # arr : given array
    # n : size of the array
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)
    for k in range(n - 1):
        if arr[k] == arr[k + 1]:
            return k + 1
        else:
            return -1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(firstRepeated(arr, n))
