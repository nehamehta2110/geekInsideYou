def absolute(I):
    if I < 0:
        return -I
    elif I > 0:
        return I
    else:
        return 0


def main():
    T = int(input())  # Input the number of testcases

    while (T > 0):
        I = int(input())  # input number
        print(absolute(I))  # Call function and print
        T -= 1  # Reduce number of testcases


if __name__ == "__main__":
    main()
