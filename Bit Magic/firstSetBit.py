# {
# Driver Code Starts
# Initial Template for Python 3


# } Driver Code Ends

# User function Template for python3

##Complete this function
def getFirstSetBit(n):
    # Your code here
    pos = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # counting the position of first set bit
    for i in range(32):
        if not (n & (1 << i)):
            pos += 1
        else:
            break

    return pos


# {
# Driver Code Starts.


def main():
    T = int(input())

    while (T > 0):
        n = int(input())

        print(getFirstSetBit(n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
