# User function Template for python3
def reverseColumns(arr, n):
    for i in range(n):
        j = 0
        k = n - 1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1


def transpose(arr, n):
    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


def rotateby90(a, n):
    # code here
    transpose(a, n)
    reverseColumns(a, n)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = line1[k]
                k += 1

        rotateby90(matrix, n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
        print()
