def printInitials(passedstring):
    splitstring = passedstring.split()
    for i in splitstring:
        result = i[0].upper()
        print(result, end=' ')


def main():
    passedstring = 'naina mehta'
    printInitials(passedstring)


if __name__ == '__main__':
    main()
