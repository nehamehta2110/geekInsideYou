import sys


class minHeap:

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.heap = [None] * capacity

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        if self.size == self.capacity:
            return False
        self.size = self.size + 1
        self.heap[self.size - 1] = key
        i = self.size - 1
        if i > 0:
            self.heapify(self.parent(i))

    def heapify(self, i):
        lt = self.left(i)
        rt = self.right(i)
        largest = i

        if lt < self.size and self.heap[lt] > self.heap[i]:
            largest = lt

        if rt < self.size and self.heap[rt] > self.heap[largest]:
            largest = rt

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

    def extract_min(self):

        if self.size == 0:
            return sys.maxsize

        if self.size == 1:
            self.size = self.size - 1
            return self.heap[0]

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1
        self.heapify(0)
        return self.heap[self.size]


def main():
    node = minHeap(5)
    l = [10, 5, 3, 2, 4]
    for i in l:
        node.insert(i)
    print(node.extract_min())


if __name__ == '__main__':
    main()
