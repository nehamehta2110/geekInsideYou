import math


def height_heap(n):
    return math.ceil(math.log(n + 1, 2)) - 1


for _ in range(int(input())):
    n = int(input())
    t = [int(i) for i in input().split()]
    print(height_heap(n))
