def transposeMatrix(arr1, n1, m1):
    """
      Function to find transpose of matrix
      n1, m1: row and column of matrices respectively
      arr1[][]: input matrix
    """

    arr2 = [[0 for x in range(n1)] for y in range(m1)]
    for i in range(m1):
        for j in range(n1):
            arr2[i][j] = arr1[j][i]

    print(arr2)


if __name__ == '__main__':
    arr1 = [[1, 2, 3],
            [5, 32, 8]]
    n1 = 2
    m1 = 3
    transposeMatrix(arr1, n1, m1)
