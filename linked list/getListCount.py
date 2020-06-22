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
        initialising the head pointer
        """
        self.head = None

    def append(self, new_data):
        """inserting data"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def getCount(self):
        """get number of elements"""
        temp = self.head
        count = 0
        while (temp):
            print(temp.data)
            count += 1
            temp = temp.next
        print("The count of elements in the list is", count)


if __name__ == '__main__':
    llist = linkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.getCount()
