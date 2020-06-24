def matSearch(arr, n, key):
    """
    Here we start from top right element,
    if the key is less than element we eleminate that column
    if the key is greater than element we increment to next row
    """

    i = 0  # first row
    j = n - 1  # last column, so as to reach top rightmost element

    while i < n and j != 0:
        if arr[i][j] == key:
            return i, j
        if arr[i][j] > key:
            j -= 1
        else:
            i += 1

    return False


if __name__ == '__main__':

    arr = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    if matSearch(arr, 4, 29):
        a, b = matSearch(arr, 4, 29)
        print("element found at row number {} and column number {}".format(a + 1, b + 1))
    else:
        print("Nope! element not found")
