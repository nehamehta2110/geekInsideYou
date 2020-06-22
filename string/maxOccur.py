# User function Template for python3
def getMaxOccurringChar(s):
    """
    Your task is to return the lexicographically smallest
    max occurring character in given string.
    Function Arguments: s (given string)
    Return Type: char or -1.
    """
    freqDict = {}
    s = list(s)
    le = len(s)
    for i in range(le - 1):
        for j in range(le - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    new_s = ''.join(s)

    for i in range(len(new_s)):
        if new_s[i] not in freqDict.keys():
            count = 1
            freqDict[new_s[i]] = count
        else:
            freqDict[new_s[i]] = freqDict[new_s[i]] + 1
    sorted_dict = sorted(freqDict.keys())
    max1 = 0
    key = ""
    for i in sorted_dict:
        if max1 < freqDict[i]:
            max1 = freqDict[i]
            key = i
        else:
            continue

    return key


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(getMaxOccurringChar(s))
