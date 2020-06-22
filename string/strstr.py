def strstr(s, p):
    """
    Your task is to return the index of the pattern
    present in the given string.

    Function Arguments: s (given text), p(given pattern)
    Return Type: Integer.
    """
    l1 = len(s)
    l2 = len(p)
    for i in range(l1 - l2 + 1):
        j = 0
        while (j < l2):
            if s[i + j] != p[j]:
                break
            j += 1
        if j == l2:
            return i
    return -1


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        s, p = input().strip().split()
        print(strstr(s, p))

# } Driver Code Ends
