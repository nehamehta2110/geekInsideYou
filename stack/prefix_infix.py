def isOperand(x):
    """
    function to check if char x is operand
    :param x: character
    """
    return (('a' <= x <= 'z') or
            ('A' <= x <= 'Z'))


def preToIn(exp):
    """
        Converts prefix expression to infix
        :param exp: expression
        :return: Infix notation
    """

    stack = []
    exp = exp[::-1]
    exp_length = len(exp)

    for i in range(exp_length):
        if isOperand(exp[i]):
            stack.append(exp[i])

        else:
            a = stack.pop()
            b = stack.pop()
            temp_exp = a + exp[i] + b
            stack.append(temp_exp)

    print(*stack)


def main():
    """driver function"""
    exp = '*+AB-CD'
    preToIn(exp)


if __name__ == '__main__':
    main()
