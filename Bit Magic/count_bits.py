# User function Template for python3
def CountBits(n):
    # code here
    # return the count
    res = 0
    for i in range(1, n + 1):
        while i != 0:
            i = i & (i - 1)
            res += 1
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        print(CountBits(int(input())))
