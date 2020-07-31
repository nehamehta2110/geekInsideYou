class Queue:

    def __init__(self):
        """
        initialisation with 2 stacks
        """
        self.s1 = []
        self.s2 = []

    def enqueue(self, element):

        # Move all elements from s1 to s2

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1
        self.s1.append(element)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        """
        pop function
        :return: element popped
        """
        # if queue is already empty
        if len(self.s1) == 0:
            print("--The queue is emptyyyy!!!")

        # return the last element and pop it
        x = self.s1[-1]
        self.s1.pop()
        return x


def main():
    """driver function"""
    q = Queue()
    q.enqueue(13)
    q.enqueue(35)
    q.enqueue(46)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()
