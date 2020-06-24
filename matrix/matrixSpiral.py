def matrixSpiral(matrix, m, n):
    """
    The algorithm is to print 1st row, last column, last row and 1st column,
    we define k and l for row index and column index respectively
    :param matrix: given matrix
    :param m: number of rows
    :param n: number of columns
    :return: spiral traversal
    """
    spiralString = ""
    k, l = 0, 0
    while k < m and l < n:
        for i in range(l, n):  # Traversing the first row
            spiralString += str(matrix[k][i]) + " "
        k += 1

        for i in range(k, m):  # Traversing the last column
            spiralString += str(matrix[i][n - 1]) + " "
        n -= 1

        if (k < m):
            for i in range(n - 1, l - 1, -1):  # Traversing the last row
                spiralString += str(matrix[m - 1][i]) + " "
            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):  # Traversing the first column
                spiralString += str(matrix[i][l]) + " "
            l += 1

    print(spiralString)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 141, 125, 146, 127, 158]]

    m = 4
    n = 6
    matrixSpiral(matrix, m, n)
