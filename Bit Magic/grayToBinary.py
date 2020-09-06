# User function Template for python3


##Complete this function
def grayToBinary(n):
    ##Your code here
    inv = 0
    while (n):
        inv = inv ^ n
        n = n >> 1
    return inv


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        print(grayToBinary(n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
