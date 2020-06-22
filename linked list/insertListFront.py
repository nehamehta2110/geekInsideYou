class Node:
    def __init__(self, data):
        """
        initialising data and next pointer
        """
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """
        initialising head of linked list
        """
        self.head = None

    def push(self, new_data):
        """
        insert element in the front
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        """
        traverses elements
        """
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.push(2)
    llist.push(3)
    llist.push(5)
    llist.printList()
