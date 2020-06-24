def multiplyMatrix(n1, m1, n2, m2, arr1, arr2):
    """
          Function to find product of matrices
          n1, m1, n2, m2: rows and columns of matrices respectively
          arr1[][], arr2[][]: two input matrices
    """

    if m1 != n2:
        return

    arr3 = [[0 for x in range(m2)] for y in range(n1)]

    for i in range(n1):
        for j in range(m1):
            for k in range(m2):
                arr3[i][j] += arr1[i][k] * arr2[k][j]

    for m in range(n1):
        for n in range(m2):
            print(arr3[m][n], end=' ')


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

        n2, m2 = map(int, input().strip().split())
        arr2 = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]

        k = 0
        for i in range(n2):
            for j in range(m2):
                arr2[i][j] = line2[k]
                k += 1

        k = 0

        multiplyMatrix(n1, m1, n2, m2, arr1, arr2)

        print()

        T -= 1


if __name__ == "__main__":
    main()
