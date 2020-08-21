def count_triplets(arr, n):
    freq = [0 for i in range(100)]

    count = 0

    for i in range(n):
        freq[arr[i]] += 1

    for x in range(n):
        for y in range(x + 1, n, 1):
            if freq[arr[x] + arr[y]]:
                count += 1

    print(count)


def main():
    test_case = int(input())

    for i in range(test_case):
        size = int(input())
        arr = list(map(int, input().split()))
        count_triplets(arr, size)


if __name__ == '__main__':
    main()
