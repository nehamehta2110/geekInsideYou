class Node:
    def __init__(self, data):
        """initialising the data and next pointer of a node"""

        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """initialising the head node of linked list"""

        self.head = None

    def insertAfter(self, prev_node, new_data):
        """inserting new node at after a node in the linked list"""

        if prev_node is None:
            print('given node not in linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        """traversing elements"""
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

    llist.insertAfter(llist.head, 8)
    llist.printList()
