def checkKthBit(n, k):
    # Your code here
    if k == 0:
        if n & 1:
            return True
        elif n & 1 == 0:
            return False

    elif n & (1 << (k - 1)):
        return True

    else:
        return False


def main():
    T = int(input())

    while T > 0:

        n = int(input())
        k = int(input())

        if checkKthBit(n, k):
            print("Yes")
        else:
            print("No")

        T -= 1


if __name__ == "__main__":
    main()
