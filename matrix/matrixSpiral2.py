def spirallyTraverse(matrix, r, c):
    # code here
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    ans = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        ans = spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()
