class Node:
    """
    Node class with data and it's pointer
    """

    def __init__(self, data):
        self.data = data  # initializing the data
        self.next = None  # initializing next as null


class linkedList:
    """
    class linked list for traversing functions
    """

    def __init__(self):
        self.head = None  # head initialized to null

    def printList(self):
        temp = self.head  # value of head stored in temp variable
        while (temp):
            print(temp.data)  # traversing the elements
            temp = temp.next  # incrementing to the next pointer


if __name__ == '__main__':
    llist = linkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
