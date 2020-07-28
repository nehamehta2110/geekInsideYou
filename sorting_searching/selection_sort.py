"""
algo:
find the minimum element and swap it with the first element
"""


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def s_sort(arr, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[j + 1]:
                min_idx = j

        arr[min_idx], arr[i] = swap(arr[min_idx], arr[i])


def main():
    arr = [11, 12, 13, 5, 6]
    N = 5
    s_sort(arr, N)
    print(arr)


if __name__ == '__main__':
    main()
