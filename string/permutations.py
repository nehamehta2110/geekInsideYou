def permut(a, l, r):
    if l == r:
        print(''.join(a), end=" ")
        return
    else:
        for i in range(l, r + 1):
            a[i], a[l] = a[l], a[i]
            permut(a, l + 1, r)
            a[i], a[l] = a[l], a[i]


def main():
    test = int(input())
    for i in range(test):
        a = str(input())
        n = len(a)
        a = list(a)
        permut(a, 0, n - 1)
        print()


if __name__ == "__main__":
    main()
