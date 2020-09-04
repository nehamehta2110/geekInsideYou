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
