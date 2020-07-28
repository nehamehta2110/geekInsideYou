"""
Algorithm: start from the second element
* compare with the sorted subarray
* shift all elements before current element if smaller & insert curent at new empty space
"""


def i_sort(arr, N):
    for i in range(1, N):
        key = arr[i]  # current element
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    arr = [11, 12, 13, 5, 6]
    N = 5
    i_sort(arr, N)
    print(arr)


if __name__ == '__main__':
    main()
