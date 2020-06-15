import math


def logCount(N):
    """
    Number of digits in a number N are given by (log base 10 of N) +1
    """
    if N != 0:
        num = math.floor(math.log10(N) + 1)
    else:
        num = 1
    return num


def main():
    N = int(input())
    print('The number of digits are {}'.format(logCount(N)))


if __name__ == '__main__':
    main()
