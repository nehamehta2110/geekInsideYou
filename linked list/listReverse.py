class Node:
    def __init__(self, data):
        """
        initializing data and next pointer
        """
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """
        initializing head node
        """
        self.head = None

    def append(self, new_data):
        """
        inserting data to the linked list
        :param new_data: new element
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        """
        traversing elements of linked list
        """
        temp = self.head
        listString = ""
        while (temp):
            listString += str(temp.data) + " "
            temp = temp.next
        print(listString)

    def reverseList(self):
        """
        reverse the linked list
        """
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


if __name__ == '__main__':
    llist = linkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.printList()
    llist.reverseList()
    llist.printList()
