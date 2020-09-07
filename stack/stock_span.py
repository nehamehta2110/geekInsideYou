def calculateSpan(a, n):
    st = []
    s = [0 for i in range(n)]
    s[0] = 1
    st.append(0)

    for i in range(n):
        while len(st) > 0 and a[st[-1]] <= a[i]:
            st.pop()
        if len(st) == 0:
            s[i] = i + 1
        else:
            s[i] = i - st[-1]

        st.append(i)
    return s


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(*calculateSpan(a, n))
