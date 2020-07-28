"""
Given an integer x.
The task is to find the square root of x. If x is not a perfect square, then return floor(√x).
"""
import math


def floorSqrt(x):
    # Your code here
    return math.floor(x ** 0.5)


# {
#  Driver Code Starts

def main():
    T = int(input())
    while T > 0:
        x = int(input())

        print(floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
