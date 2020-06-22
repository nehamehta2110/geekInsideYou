class Node:
    def __init__(self, data):
        """initialising the data and next pointer of a node"""

        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """initialising the head node of linked list"""

        self.head = None

    def append(self, new_data):
        """inserting new node at the end of the list"""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printlist(self):
        """traversing the elements"""
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.append(2)
    llist.append(4)
    llist.append(6)
    llist.printlist()
