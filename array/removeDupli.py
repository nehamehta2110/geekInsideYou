# Remove duplicate elements in array
def remove_duplicate(n, arr):
    arr = sorted(arr)
    arr1 = []
    for i in range(n - 1):
        if arr[i + 1] == arr[i]:
            pass
        else:
            arr1.append(arr[i])
    arr1.append(arr[-1])
    arr = arr1
    return len(arr), arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n, arr = remove_duplicate(n, arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()
