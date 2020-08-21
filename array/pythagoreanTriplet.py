def pythagorean_triplet(arr, n):
    freq = {}

    for i in range(n):
        freq[arr[i] * arr[i]] = 1

    count = 0

    for i in range(n):
        for j in range(i - 1, n):

            if (arr[i] * arr[i] + arr[j] * arr[j]) in freq.keys():
                count += 1

    if count != 0:
        print('Yes')
        return
    print('No')


def main():
    test_case = int(input())
    for i in range(test_case):
        n = int(input())
        arr = list(map(int, input().split()))

        pythagorean_triplet(arr, n)


if __name__ == '__main__':
    main()
