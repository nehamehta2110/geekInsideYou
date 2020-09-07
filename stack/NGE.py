def nextLargerElement(arr, n):
    # code here
    st = []
    nge = []
    st.append(arr[n - 1])
    nge.append(-1)
    for i in range(n - 2, -1, -1):
        while len(st) != 0 and st[-1] <= arr[i]:
            st.pop()
        if len(st) == 0:
            nge.append(-1)
        else:
            nge.append(st[-1])
        st.append(arr[i])

    return nge[::-1]


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())

        a = list(map(int, input().strip().split()))
        res = nextLargerElement(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
