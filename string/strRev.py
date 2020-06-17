# User function Template for python3


def reverseWords(s):
    """
    Your task is to reverse the string without reversing
    individual words and return the obtained string.

    Function Arguments: s (given string)
    Return Type: string
    """
    s = s.split('.')
    s = s[::-1]
    word = '.'.join(s)
    print(word)


def main():
    t = int(input())
    for i in range(t):
        s = str(input())
        reverseWords(s)


if __name__ == '__main__':
    main()
