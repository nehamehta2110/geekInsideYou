def subarray_sum(arr, n, sum):
    current_sum = 0
    map = {}

    for i in range(n):

        current_sum = current_sum + arr[i]

        if sum == current_sum:
            print('{} {}'.format(1, i + 1))
            return

        if (current_sum - sum) in map:
            print('{} {}'.format(map[current_sum - sum] + 2, i + 1))
            return

        map[current_sum] = i
    print(-1)


def main():
    test_case = int(input())

    for i in range(test_case):
        size = list(map(int, input().split()))
        n = size[0]
        sum = size[1]
        arr = list(map(int, input().split()))
        subarray_sum(arr, n, sum)


if __name__ == '__main__':
    main()
