def isSparse(n):
    # Your code here
    if n & (n >> 1):
        return False

    return True


def main():
    T = int(input())

    while T > 0:

        n = int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T -= 1


if __name__ == "__main__":
    main()
