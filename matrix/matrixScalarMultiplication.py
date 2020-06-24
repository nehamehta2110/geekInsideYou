def scalarMultiply(A, M, N, k):
    """
      Function to find scalar product of matrix
      M, N: row and column of matrix respectively
      A[][]: input matrix
      k: scalar to multiply
    """

    for i in range(M):
        for j in range(N):
            A[i][j] = k * A[i][j]
    print(A)


if __name__ == '__main__':
    A = [[1, 3, 8],
         [4, 2, 0]]
    M = 2
    N = 3
    k = 2
    scalarMultiply(A, M, N, k)
