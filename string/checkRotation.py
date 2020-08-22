def check_rotate(s1, s2):
    if len(s1) != len(s2):
        print('0')
        return 0
    if s2 == s1[2:] + s1[:2] or s2 == s1[-2:] + s1[:-2]:
        print('1')
        return 1


def main():
    test = int(input())
    for i in range(test):
        s1 = str(input())
        s2 = str(input())
        check_rotate(s1, s2)


if __name__ == '__main__':
    main()
