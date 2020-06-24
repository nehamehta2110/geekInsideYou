def subtractMatrix(A, B, N):
    """
      Function to SUBTRACT two matrices
      N: rows and columns of matrices respectively
      A, B: two input matrices
    """

    C = A[:][:]

    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] - B[i][j]
    print(C)


if __name__ == '__main__':
    A = [[6, 7, 8],
         [7, 8, 9],
         [8, 9, 10]]
    B = [[1, 2, 3],
         [2, 0, 4],
         [3, 4, 1]]
    N = 3

    subtractMatrix(A, B, N)
