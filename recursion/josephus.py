def josephus(n, k):
    """
    Given the total number of persons n and a number k which indicates
    that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
    The task is to choose the safe place in the circle so that
    when you perform these operations starting from 1st place
    in the circle, you are the last one remaining and survive.
    """
    # Your code here
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


def main():
    T = int(input())

    while (T > 0):
        nk = [int(x) for x in input().strip().split()]
        n = nk[0]
        k = nk[1]

        print(josephus(n, k))

        T -= 1


if __name__ == "__main__":
    main()
