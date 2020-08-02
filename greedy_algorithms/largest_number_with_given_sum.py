"""
How to find the largest number with given digit sum s and number of digits d?
Input  : s = 9, n = 2
Output : 90
There is a Greedy approach to solve the problem.
The idea is to one by one fill all digits from leftmost to rightmost.
We compare the remaining sum with 9 if the remaining sum is more than 9,
we put 9 at the current position, else we put the remaining sum.
Since we fill digits from left to right, we put the highest digits on the left side,
hence get the largest number.
"""


def findLargestNumber(n, s):
    if s == 0:
        if n == 1:
            print("--The largest number is 0")
            return
        else:
            print("--Not possible")
            return

    if s > 9 * n:
        print("--Not possible")
        return

    result = [0] * n

    for i in range(0, n):

        if s >= 9:
            result[i] = 9
            s = s - 9

        else:
            result[i] = s
            s = 0

    print("--The largest number is:")
    for j in range(n):
        print(result[j], end="")


def main():
    s = 9
    n = 2
    findLargestNumber(n, s)


if __name__ == '__main__':
    main()
