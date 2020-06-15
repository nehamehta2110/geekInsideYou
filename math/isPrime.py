def isPrime(N):
    if N == 2:
        return True
    else:
        for i in range(2, N):
            if N % i == 0:
                return False
        return True


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        if (isPrime(N)):
            print("Yes")
        else:
            print("No")

        T -= 1


if __name__ == "__main__":
    main()
