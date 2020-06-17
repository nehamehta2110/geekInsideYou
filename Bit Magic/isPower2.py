import math


def isPowerofTwo(n):
    """
    Given a positive integer N. The task is to
    check if N is a power of 2. More formally,
    check if N can be expressed as 2x for some x.
    :param n: input number
    :return: boolean true/false
    """
    if n > 0:
        x = math.log(n, 2)
        for i in range(int(x) - 1, int(x) + 1):
            if 2 ** i == n:
                return True

        return False
    else:
        return False


def main():
    T = int(input())

    while (T > 0):

        n = int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")

        T -= 1


if __name__ == "__main__":
    main()
