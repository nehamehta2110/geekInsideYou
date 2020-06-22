class Node:
    def __init__(self, data):
        """initialising the data and next pointer of a node"""

        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """initialising the head node"""

        self.head = None

    def push(self, new_data):
        """inserting the data in the linked list"""

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteAt(self, position):
        """delete data at a given index in linked list"""

        if self.head is None:
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def printList(self):
        """traversing the elements"""
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.push(1)
    llist.push(2)
    llist.push(7)
    llist.push(4)
    llist.printList()
    print("after deletion")
    llist.deleteAt(2)
    llist.printList()
