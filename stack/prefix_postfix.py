def prefix_to_postfix(s):
    """
    conversion of prefix expression to postfix
    """

    operators = {'*', '+', '-'}
    stack = []

    s = s[::-1]

    for i in s:

        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temporary_str = a + b + i
            stack.append(temporary_str)

        else:
            stack.append(i)

    print(*stack)


def main():
    """driver function"""

    s = '*+AB-CD'
    prefix_to_postfix(s)


if __name__ == '__main__':
    main()
