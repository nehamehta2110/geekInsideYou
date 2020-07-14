def is_k_bit(num, k):
    """
    To check whether kth bit is set or not
    :param num:
    :param k:
    :return: True/False
    """

    for i in range(1, 2 ** num):
        for j in range(num):
            if num & (1 << j):
                print("TRUE")
    print("FALSE")


def main():
    nums = [4, 4, 500]
    k_arr = [0, 2, 3]
    for i in range(3):
        is_k_bit(nums[i], k_arr[i])


if __name__ == '__main__':
    main()
