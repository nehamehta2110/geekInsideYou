def boundary_matrix(mat, r, c):
    if r == 1:
        for i in range(c):
            print(mat[0][i], end=' ')
    elif c == 1:
        for i in range(r):
            print(mat[i][0], end=' ')
    else:
        for i in range(c):
            print(mat[0][i], end=' ')

        for i in range(1, r):
            print(mat[i][c - 1], end=' ')

        for i in range(c - 2, -1, -1):
            print(mat[r - 1][i], end=' ')

        for i in range(r - 2, 0, -1):
            print(mat[i][0], end=' ')
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

        boundary_matrix(mat, r=n, c=n)
