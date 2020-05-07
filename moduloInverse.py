def moduloInverse(a, M):
    a = a % M
    for i in range(1, M):
        if (a * i) % M == 1:
            return i
    return 1


def main():
    a = 3
    M = 11
    print(moduloInverse(a, M))


if __name__ == '__main__':
    main()
