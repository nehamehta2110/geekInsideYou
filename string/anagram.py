def isAnagram(a, b):
    """
    Your task is to check given two strings
       are anagrams or not.
       a,b: given strings

       Return True or False accordingly.

       -> You don't need to print anything.Return type of function
       is boolean.
    """
    a = list(a)
    l1 = len(a)

    for i in range(l1 - 1):
        for j in range(l1 - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    new_a = ''.join(a)

    b = list(b)
    l2 = len(b)
    for i in range(l2 - 1):
        for j in range(l2 - i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    new_b = ''.join(b)

    if new_a == new_b:
        return True
    else:
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if (isAnagram(a, b)):
            print("YES")
        else:
            print("NO")
