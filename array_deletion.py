def arr_del(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            print("Value to be deleted at position", i)
            return i


def main():
    arr = [86, 25, 63, 57, 32]
    value = 57
    ix = arr_del(arr, value)
    for j in range(ix + 1, len(arr)):
        arr[j - 1] = arr[j]
    arr1 = []
    for k in range(len(arr) - 1):
        arr1.append(arr[k])
    print(arr1)


if __name__ == '__main__':
    main()
