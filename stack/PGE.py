def nextLargerElement(arr, n):
    # code here
    st = []
    pge = []
    st.append(arr[0])
    pge.append(-1)
    for i in range(1, n):
        while len(st) != 0 and st[-1] <= arr[i]:
            st.pop()
        if len(st) == 0:
            pge.append(-1)
        else:
            pge.append(st[-1])
        st.append(arr[i])

    return pge


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())

        a = list(map(int, input().strip().split()))
        res = nextLargerElement(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
