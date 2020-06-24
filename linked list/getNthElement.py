class Node:
    def __init__(self, data):
        """
        initializing the data and next pointer
        """
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """
        initializing the head node
        """
        self.head = None

    def append(self, new_data):
        """
        insert data in the linked list
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def getNthNode(self, index):
        """
        traversing the list to get the nth node
        """
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            count += 1
            temp = temp.next
        return False


if __name__ == '__main__':
    llist = linkedList()
    llist.append(3)
    llist.append(5)
    llist.append(2)
    llist.append(9)
    pos = 3
    print("The element at index {} in the linked list is {}".format(pos, llist.getNthNode(pos)))
