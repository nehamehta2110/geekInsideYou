# User function Template for python3
def minCost(a, n):
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :return: Integer
    '''
    # code here
    heap = a
    cost = 0
    heapq.heapify(heap)
    while len(heap) >= 2:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = cost + first + second
        heapq.heappush(heap, first + second)

    return cost


import heapq

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(minCost(a, n))
