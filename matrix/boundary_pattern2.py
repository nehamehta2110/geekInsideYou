def boundary_matrix(a, m, n):
    for i in range(m):
        for j in range(n):
            if i == 0:
                print(a[i][j], end=' ')
            elif i == m - 1:
                print(a[i][j], end=' ')
            elif j == 0:
                print(a[i][j], end=' ')
            elif j == n - 1:
                print(a[i][j], end=' ')
    print()


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        k = 0
        mat = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1

        boundary_matrix(mat, n, n)
