def pattern_match(text, pattern):
    """
    matches pattern in a given string
    :param text: main string
    :param pattern: pattern string that has to matched
    :return: index of pattern matches
    """
    x = len(text)
    y = len(pattern)

    for i in range(x - y + 1):
        j = 0
        while (j < y):
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == y:
            print('pattern found at index', i)


def main():
    text = 'AABCAJKDWAABCIIJSAABC'
    pattern = 'AABC'
    pattern_match(text, pattern)


if __name__ == '__main__':
    main()
