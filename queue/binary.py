# User function Template for python3
import atexit
import io
import sys

"""
Function Arguments :
@param  : n (given number)
@return : list of all the binary numbers till n.
"""


def GenerateBinary(n):
    # code here
    q = []
    r = []
    q.append("1")
    while n > 0:
        n -= 1
        fr = q[0]
        del q[0]
        r.append(fr)
        fr1 = fr
        q.append(fr + "0")
        q.append(fr1 + "1")

    return r


# {
#  Driver Code Starts
# Initial Template for Python 3

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
        n = int(input())
        res = GenerateBinary(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
