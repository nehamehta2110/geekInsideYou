def isValidIP(s):
    # code here
    s = s.split('.')
    result = []
    if len(s) != 4:
        result.append('0')
    else:
        for i in s:
            if i.startswith('0') and i != '0':
                result.append('0')
            else:
                if 0 <= int(i) <= 255:
                    result.append('1')
    if '0' in result:
        return False
    else:
        return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        if (isValidIP(s)):
            print(1)
        else:
            print(0)
