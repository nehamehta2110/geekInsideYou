from sys import maxsize


def contiguous_array_sum(A, N):
    """
    Function to determine starting index, ending index of maximum sum subarray
    problem using Kadane's algorithm, which states that keep track of positive segments
    while ignoring the negative segments
    :param A: array input
    :param N: length of array
    :return: s, e, sum
    """
    max_sum = -maxsize - 1
    max_end = 0
    s = 0
    end = 0
    start = 0

    for i in range(N):
        max_end += A[i]

        if max_sum < max_end:
            max_sum = max_end
            start = s
            end = i

        if max_end < 0:
            max_end = 0
            s = i + 1

    return start, end, max_sum


def main():
    A = [-2, -3, 4, 1, -2, 1, 5, -3]
    start, end, max_sum = contiguous_array_sum(A, len(A))
    print("-- starting index", start)
    print("-- ending index", end)
    print("maximum sub array sum:", max_sum)


if __name__ == '__main__':
    main()
