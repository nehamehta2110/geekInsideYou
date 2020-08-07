def checkMinHeap(arr, n):
    """
    This function checks whether a given tree is a min heap
    :param arr: tree in form of array
    :param n: number of nodes
    :return:
    """

    for i in range((n // 2) - 1, -1, -1):

        if arr[i] > arr[(i * 2) + 1]:
            return False

        if (i * 2) + 2 < n:

            if arr[i] > arr[(i * 2) + 2]:
                return False

    return True


def main():
    arr = [10, 15, 14, 25, 30]
    n = len(arr)
    if checkMinHeap(arr, n):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
