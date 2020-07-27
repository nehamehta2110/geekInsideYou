"""
In linear search, each element is traversed one by one until match is found!!
"""


def lsearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


def main():
    n = int(input())
    arr = input("Enter arr separated by space")
    arr = arr.strip().split()
    x = input("enter key")
    if lsearch(arr, n, x) != -1:
        print("--Yay! found your key at index", lsearch(arr, n, x))
    else:
        print("--Oops! not sure what you are looking for")


if __name__ == '__main__':
    main()
