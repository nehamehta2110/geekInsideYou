# User function Template for python3
def nearlySorted(a, n, k):
    '''
    :param a: given array
    :param n: size of a
    :param k: max absolute distance of value from its sorted position
    :return: sorted list
    '''
    heap = a[:k + 1]
    heapq.heapify(heap)

    ind = 0

    for i in range(k + 1, n):
        a[ind] = heapq.heappop(heap)
        heapq.heappush(heap, a[i])
        ind += 1

    while (heap):
        a[ind] = heapq.heappop(heap)
        ind += 1

    return a


import heapq

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        print(*nearlySorted(a, n, k))
