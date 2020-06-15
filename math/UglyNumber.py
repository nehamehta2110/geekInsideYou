def divide(no, div):
    while no % div == 0:
        no = no / div
    return no


def isUgly(num):
    num = divide(num, 2)
    num = divide(num, 3)
    num = divide(num, 5)
    return 1 if num == 1 else 0


def nthUgly(n):
    count = 1
    i = 1

    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


def main():
    print(nthUgly(15))


if __name__ == '__main__':
    main()
