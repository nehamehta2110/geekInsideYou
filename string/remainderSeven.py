def remainderWith7(str):
    """
    Given a number as string(n) ,your task is
    to complete the function remainderWith7 which returns
    an integer which denotes the remainder of the number when its divided by 7.
    """

    str = int(str)
    res = str % 7
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))
