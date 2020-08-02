"""
Reverse a string using Stack
An string of words is given, the task is to reverse the string using stack.
Input:
1
GeeksQuiz
Output:
ziuQskeeG
"""


def reverse(string):
    # Add code here
    s = ""
    string = list(string)
    n = len(string)
    while n != 0:
        s += string.pop()
        n -= 1

    return s


# {
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
# } Driver Code Ends
