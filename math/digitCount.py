def checkZero(num):
    if num != 0:
        return True
    else:
        return False


def main():
    nu = int(input('Enter your number'))
    digitCounter = 0
    if not checkZero(nu):
        digitCounter += 1

    while checkZero(nu):
        digitCounter += 1
        nu = nu // 10
    print("The number of digits are {}".format(digitCounter))


if __name__ == "__main__":
    main()
