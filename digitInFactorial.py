def factorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    else:
        return factorial(N - 1) * N


def digitsInFactorial(N):
    # Your code here
    ans = factorial(N)
    digitC = 0
    while ans != 0:
        digitC += 1
        ans = ans // 10

    return digitC


def main():
    T = int(input())

    while (T > 0):
        N = int(input())

        print(digitsInFactorial(N))

        T -= 1


if __name__ == "__main__":
    main()
