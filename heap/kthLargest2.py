# User function Template for python3
from heapq import heapify, heappush, heappop


class Solution:

    def kLargest(self, arr, n, k):
        # code here
        b = arr[:k]
        heapify(b)
        b = list(b)
        for i in range(k, n):
            if b[0] < arr[i]:
                heappop(b)
                heappush(b, arr[i])
        b.sort(reverse=True)
        return b


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1
