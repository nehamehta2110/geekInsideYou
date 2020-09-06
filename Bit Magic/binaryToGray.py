def greyConverter(n):
    return n ^ (n >> 1)


def main():
    T = int(input())

    while T > 0:
        n = int(input())
        print(greyConverter(n))
        T -= 1


if __name__ == "__main__":
    main()
