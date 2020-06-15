import math


def quadraticRoots(a, b, c):
    # Your code here
    if b * b < 4 * a * c:
        print('Imaginary')

    else:
        print(math.floor((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)),
              math.floor((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)))


def main():
    T = int(input())

    while (T > 0):
        abc = [int(x) for x in input().strip().split()]
        a = abc[0]
        b = abc[1]
        c = abc[2]

        quadraticRoots(a, b, c)

        T -= 1


if __name__ == "__main__":
    main()
