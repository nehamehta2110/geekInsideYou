class Node:
    def __init__(self, data):
        """initialising data and next pointer"""
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """initialising head node"""
        self.head = None

    def append(self, new_data):
        """inserting data at the end"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteList(self):
        """delete a linked list"""
        current = self.head
        while (current):
            prev = current.next
            del current.data
            current = prev

    def printList(self):
        """traversing a list"""
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.printList()
    print(". . .hold on! deleting linked list")
    llist.deleteList()
    print("Yayyy! Deleted")
