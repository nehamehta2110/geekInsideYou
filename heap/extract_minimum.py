from sys import maxsize


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
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def pri(self):
        for i in range(self.size):
            print(self.heap[i], end=' ')
        print()

    def heapify(self, i):
        lt = self.left(i)
        rt = self.right(i)
        smallest = i

        if lt < self.size and self.heap[lt] < self.heap[i]:
            smallest = lt

        if rt < self.size and self.heap[rt] < self.heap[smallest]:
            smallest = rt

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapify(smallest)

    def extract_min(self):

        if self.size == 0:
            return maxsize

        if self.size == 1:
            self.size = self.size - 1
            return self.heap[0]

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1
        self.heapify(0)
        return self.heap[self.size]


def main():
    node = minHeap(6)
    l = [10, 5, 3, 2, 4, 1]
    for i in l:
        node.insert(i)
    node.pri()
    print('-This is the extracted node value:', node.extract_min())
    node.pri()


if __name__ == '__main__':
    main()
