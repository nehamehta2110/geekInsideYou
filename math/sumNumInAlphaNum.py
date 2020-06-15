def sumNum(inputstring):
    sum = 0
    for i in inputstring:
        if i.isdigit():
            sum += int(i)
    return sum


def main():
    print(sumNum(inputstring='bcgeek1g45'))


if __name__ == '__main__':
    main()
