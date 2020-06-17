def printNos(N):
    # Your code here
    if N == 0:
        pass
    elif N == 1:
        print(1)
    else:
        print(N)
        printNos(N - 1)


def main():
    T = int(input())

    while (T > 0):
        N = int(input())

        printNos(N)
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
