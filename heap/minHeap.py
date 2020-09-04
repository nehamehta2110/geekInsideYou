"""
Implementing basic operations of min heap
"""


class minheap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [None] * capacity

    def parent(self, i):
        return i - 1 // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

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

    def insert(self, key):
        if self.size == self.capacity:
            return False
        self.size = self.size + 1
        self.heap[self.size - 1] = key
        i = self.size - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def show_heap(self):
        print(self.heap)


def main():
    node = minheap(5)
    node.insert(2)
    node.insert(10)
    node.insert(3)
    node.insert(33)
    node.insert(9)
    node.show_heap()


if __name__ == '__main__':
    main()
