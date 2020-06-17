def multiply(a, b):
    """
    Given two numbers as stings s1 and s2 your task is to multiply them.
    You are required to complete the function multiplyStrings which takes
    two strings s1 and s2 as its only argument and returns their product
    as strings.
    """
    a = int(a)
    b = int(b)
    return str(a * b)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        print(multiply(a.strip(), b.strip()))
