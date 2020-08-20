def missing_element(arr, n):
    summation = sum(arr)
    actual_summation = (n * (n + 1)) / 2

    return int(actual_summation) - summation


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(missing_element(arr, n))
