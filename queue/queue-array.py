class Queue:
    def __init__(self, capacity):
        """
        initialisation of queue with front and rear and max capacity
        """
        self.capacity = capacity
        self.front = self.size = 0
        self.Q = [None] * capacity
        self.rear = capacity - 1

    def isEmpty(self):
        """
        check if the queue is empty
        {Underflow}
        """
        return self.size == 0

    def isFull(self):
        """
        check if the queue is full
        {Overflow}
        """
        return self.size == self.capacity

    def enQueue(self, item):
        """
        function to insert an item to queue at the rear end {FIFO}
        """
        if self.isFull():
            print("Overflow!")

        self.rear = (self.rear + 1) % self.capacity

        self.Q[self.rear] = item
        print("--enqueued item", str(self.Q[self.rear]))
        self.size = self.size + 1

    def deQueue(self):
        """
        function to delete an item from queue at the front end {FIFO}
        """
        if self.isEmpty():
            print("Underflow!")

        print("--dequeued item", str(self.Q[self.front]))
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def front_element(self):
        """
        Function to print the front element
        """
        if self.isEmpty():
            print("Underflow!")
            return
        return self.Q[self.front]

    def rear_element(self):
        """
        Function to print the rear element
        """
        if self.isEmpty():
            print("Underflow!")
            return
        return self.Q[self.rear]


def main():
    """driver code"""
    q = Queue(20)
    q.isEmpty()
    q.enQueue(9)
    q.enQueue(10)
    q.enQueue(11)
    q.front_element()
    q.rear_element()
    q.deQueue()
    print(q.front_element())


if __name__ == '__main__':
    main()
