"""
sort based on adjacent elements
"""


def b_sort(arr, N):
    for i in range(N - 1):
        for j in range(0, N - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def main():
    arr = [11, 12, 13, 5, 6]
    N = 5
    b_sort(arr, N)
    print(arr)


if __name__ == '__main__':
    main()
