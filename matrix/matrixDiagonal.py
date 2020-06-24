def diagonalMatrix(n1, m1, arr1):
    """
      Function to find diagonal of matrices
      n1, m1: rows and columns of matrix
      arr1[][]: input matrix
    """

    # Your code here
    if n1 != m1:
        return
    for i in range(n1):
        for j in range(m1):
            if i == j:
                print(arr1[i][j])


def main():
    T = int(input())
    while (T > 0):
        n1, m1 = map(int, input().strip().split())
        arr1 = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]

        k = 0
        for i in range(n1):
            for j in range(m1):
                arr1[i][j] = line1[k]
                k += 1

        k = 0

        print(arr1)

        diagonalMatrix(n1, m1, arr1)
        print()

        T -= 1


if __name__ == "__main__":
    main()
