# User function Template for python3
"""
Function Arguments :
@param  : s (given string containing parenthesis)
@return : boolean True or False
"""


def ispar(s):
    # code here
    st = []
    for i in s:
        if i in ['(', '{', '[']:
            st.append(i)

        else:
            if not st:
                return False
            current_char = st.pop()
            if current_char == '(':
                if i != ")":
                    return False
            if current_char == '{':
                if i != "}":
                    return False
            if current_char == '[':
                if i != "]":
                    return False

    if st:
        return False

    return True


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        # n,k = map(int,imput().strip().split())
        # a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")

# } Driver Code Ends
