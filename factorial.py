# factorial of a number
def fact(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    else:
        return fact(N - 1) * N


if __name__ == '__main__':
    N = int(input('Enter number'))
    print(fact(N))
