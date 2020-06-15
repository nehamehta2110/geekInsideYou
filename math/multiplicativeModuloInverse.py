def modInverse(a, m):
    for i in range(1, m):
        if (i * a) % m == 1:
            return i
    return -1


def main():
    T = int(input())

    while (T > 0):
        am = [int(x) for x in input().strip().split()]
        a = am[0]
        m = am[1]
        print(modInverse(a, m))

        T -= 1


if __name__ == "__main__":
    main()
