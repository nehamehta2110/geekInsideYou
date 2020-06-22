class Node:
    def __init__(self, data):
        """initialising data and next pointer"""
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """initialising head node"""
        self.head = None

    def delete_key(self, key):
        """
        deleting a given element
        """
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while (temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        """traversing the elements"""

        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printList()
    llist.delete_key(2)
    llist.printList()
