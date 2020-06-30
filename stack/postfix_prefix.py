def post_to_pre(exp):
    """
    Converts postfix expression to prefix
    :param exp: expression
    :return: Prefix notation
    """
    operators = {'/', '*', '-'}
    stack = []

    len_exp = len(exp)

    for i in range(len_exp):

        if exp[i] in operators:
            a = stack.pop()
            b = stack.pop()
            temp = exp[i] + b + a
            stack.append(temp)

        else:
            stack.append(exp[i])

    print(*stack)


def main():
    """
    driver function
    """
    exp = "ABC/-AK/L-*"
    post_to_pre(exp)


if __name__ == '__main__':
    main()
