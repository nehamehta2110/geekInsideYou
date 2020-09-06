def countBitsFlip(a, b):
    res = a ^ b

    def count_bits(n):
        c = 0
        while n:
            n = n & (n - 1)
            c += 1
        return c

    return count_bits(res)


def main():
    T = int(input())

    while T > 0:
        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        print(countBitsFlip(a, b))
        T -= 1


if __name__ == "__main__":
    main()
