# User function Template for python3
class Queue:
    def __init__(self, capacity):
        """
        initialisation of queue parameters
        :param capacity: total size of the queue
        """
        self.front = 0
        self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def enqueue(self, element):
        """
        function to push element to queue
        :param element: value to be pushed
        :return: if Overflow condition
        """
        if self.isFull():
            print("--Overflow!!!")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = element
            self.size = self.size + 1
            print("--({}) enqueued in the queue".format(element))

    def dequeue(self):
        """
            function to pop element from queue
            :return: if Underflow condition
        """
        if self.isEmpty():
            print("--Underflow!!!")
            return
        else:
            print("--({}) dequeued from the queue".format(self.Q[self.front]))
            self.front = (self.front + 1) % self.capacity
            self.size = self.size - 1

    def q_front(self):
        """
        function to get the front element
        :return: false if empty
        """
        if self.isEmpty():
            return False
        else:
            print("--The front element is ", self.Q[self.front])

    def q_rear(self):
        """
        function to get the rear element
        :return: false if empty
        """
        if self.isEmpty():
            return False
        else:
            print("--The rear element is ", self.Q[self.rear])

    def isFull(self):
        """-
        checker function to check is queue is full
        :return: true if full
        """
        if self.size == self.capacity:
            return True
        return False

    def isEmpty(self):
        """
        checker function to check is queue is empty
        :return: true if empty
        """
        if self.size == 0:
            return True
        return False

    def printQueue(self):
        print(*self.Q)

    def reverseQueueFirstK(self, k):
        """
        reverse the first k elements of the queue
        """
        if k <= 0:
            return
        if self.size == 0 or k > self.size:
            return

        stack = []

        while k != 0:
            stack.append(self.Q[self.front])
            self.dequeue()
            k -= 1

        while len(stack) != 0:
            self.enqueue(stack[-1])
            stack.pop()


def main():
    q = Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    q.printQueue()
    q.reverseQueueFirstK(5)
    q.printQueue()


if __name__ == '__main__':
    main()
