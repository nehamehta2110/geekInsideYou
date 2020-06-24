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

    def get_int_occur(self, search_key):
        """
        traversing the list to get the nth node
        """
        temp = self.head
        frequency = 0
        while temp:
            if temp.data == search_key:
                frequency += 1
            temp = temp.next
        return frequency


if __name__ == '__main__':
    llist = linkedList()
    llist.append(3)
    llist.append(5)
    llist.append(2)
    llist.append(9)
    llist.append(3)
    llist.append(6)
    llist.append(3)
    llist.append(8)
    key = 3
    print("The frequency of {} in the linked list is {}".format(key, llist.get_int_occur(key)))
