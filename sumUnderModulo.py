def sumUnderModulo(a, b):
    """
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    """
    M = 1000000007
    return (a % M + b % M) % M


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a, b = map(int, input().strip().split())
        print(sumUnderModulo(a, b))
