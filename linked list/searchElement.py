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

    def append(self, new_data):
        """
        insert elements at the last of list
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def searchElement(self, key):
        """searches key in the list"""
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        return False

    def getCount(self):
        """traverses the list"""
        temp = self.head
        count = 0
        while (temp):
            print(temp.data)
            count += 1
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.getCount()
    if llist.searchElement(2):
        print("Yep. . You found me!")
    else:
        print("Nope! I don't exist")
