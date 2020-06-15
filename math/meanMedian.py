def meanNum(arr):
    b = len(arr)
    sum = 0
    for i in arr:
        sum += i
    meanValue = float(sum / b)
    return meanValue


def medianNum(arr):
    arr.sort()
    l = len(arr)
    if l % 2 != 0:
        median = float(arr[int(l / 2)])
    else:
        median = float(arr[int(l / 2)] + arr[int((l / 2) - 1)]) / 2.0
    return median


if __name__ == '__main__':
    arr = [2, 36, 15, 82, 7]
    print('mean is {}'.format(meanNum(arr)))
    print('median is {}'.format(medianNum(arr)))
