def mergeArrays(a, b, n, m):
    """
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    """
    new = a + b
    new = list(set(new))
    new = sorted(new)
    return new


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        li = mergeArrays(a, b, n, m)
        for val in li:
            print(val, end=' ')
        print()
