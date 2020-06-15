def arr_rev_temp(arr, length):
    arr_temp = []
    for i in range(length):
        len = length - 1
        arr_temp.append(arr[len - i])
    return arr_temp


def main():
    arr = ['57', '28', '7', '97', '14']
    length = len(arr)
    print(arr_rev_temp(arr, length))


if __name__ == '__main__':
    main()
