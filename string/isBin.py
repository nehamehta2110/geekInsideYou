def isBinary(str):
    removal = ['2', '3', '4', '5', '6', '7', '8', '9']
    for i in removal:
        if i in str:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print(1)
        else:
            print(0)
