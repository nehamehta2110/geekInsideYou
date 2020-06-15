import math


def cToF(C):
    return (C * (9 / 5)) + 32


def main():
    T = int(input())

    while (T > 0):
        C = int(input())
        print(math.floor(cToF(C)))
        T -= 1


if __name__ == "__main__":
    main()
