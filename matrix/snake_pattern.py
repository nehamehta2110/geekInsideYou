def snake_pattern(mat, n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                print(mat[i][j], end=' ')
        else:
            for j in range(n - 1, -1, -1):
                print(mat[i][j], end=' ')
    print()


test_case = int(input())
for i in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    mat = [[0 for j in range(n)] for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = arr[k]
            k += 1
    snake_pattern(mat, n)
