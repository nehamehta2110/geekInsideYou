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

    def pri(self):
        for i in range(self.size):
            print(self.heap[i], end=' ')

    def decrease_key(self, i, key):
        self.heap[i] = key
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
    node.decrease_key(2, 4)
    node.show_heap()


if __name__ == '__main__':
    main()
