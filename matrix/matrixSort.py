def matrixSort(A, n1, n2):
    """
      Function to sort the matrix
      n1, n2: row and column of matrix respectively
      A: input matrix
    """

    temp = [0] * (n1 * n2)

    k = 0

    for i in range(n1):
        for j in range(n2):
            temp[k] = A[i][j]
            k += 1

    temp.sort()
    k = 0

    for m in range(n1):
        for n in range(n2):
            A[m][n] = temp[k]
            k += 1

    print(A)


if __name__ == '__main__':
    A = [[18, 4, 28],
         [62, 75, 2],
         [11, 3, 7]]
    n1, n2 = 3, 3
    matrixSort(A, n1, n2)
