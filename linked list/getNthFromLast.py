class Node:
    def __init__(self, data):
        """
        initialising the data and next pointer
        """
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        """
        initialising the head node
        """
        self.head = None

    def push(self, new_data):
        """
        insert data into linked list
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getNthFromLast(self, index):
        """
        get nth element from the end
        """
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        print(count)
        if index > count:
            return False
        index1 = count - index
        count1 = 0
        temp = self.head

        while (temp):
            if count1 == index1:
                print(temp.data)
            count1 += 1
            temp = temp.next


if __name__ == '__main__':
    llist = linkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.getNthFromLast(4)
