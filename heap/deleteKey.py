from sys import maxsize


class minheap:

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

    def decrease_key(self, i, key):
        self.heap[i] = key
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

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

    def delete_key(self, i):
        self.decrease_key(i, -maxsize)
        self.extract_min()

    def show_heap(self):
        for i in range(self.size):
            print(self.heap[i], end=' ')
        print()


def main():
    node = minheap(5)
    node.insert(2)
    node.insert(10)
    node.insert(3)
    node.insert(33)
    node.insert(9)
    node.show_heap()
    node.decrease_key(2, 4)
    node.show_heap()
    node.delete_key(2)
    node.show_heap()


if __name__ == '__main__':
    main()
