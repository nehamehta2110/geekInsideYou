class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.rear = self.front = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, key):
        temp = Node(key)
        if self.rear is None:
            self.rear = self.front = temp

        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None


def main():
    q = queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))


if __name__ == '__main__':
    main()
