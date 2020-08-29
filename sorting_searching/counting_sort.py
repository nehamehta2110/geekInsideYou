def counting_sort(arr, n):
    count = [0 for i in range(9)]
    output = [0 for i in range(n)]

    for i in arr:
        count[i] += 1

    for i in range(9):
        count[i] += count[i - 1]

    for i in range(n):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


arr = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(arr, len(arr)))
