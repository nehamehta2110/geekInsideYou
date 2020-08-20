def count_last_one(s):
    if '1' not in s:
        return -1
    else:
        s = s[::-1]
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                return n - i - 1


def main():
    test_case = int(input())
    for i in range(test_case):
        case = str(input())
        print(count_last_one(case))


if __name__ == '__main__':
    main()
