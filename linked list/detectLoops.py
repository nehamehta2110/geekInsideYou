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

    def detectCycle(self):
        """
        get nth element from the end
        """
        s = set()
        temp = self.head

        while (temp):
            if temp in s:
                return True

            s.add(temp)
            temp = temp.next

        return False


if __name__ == '__main__':
    llist = linkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.head.next.next.next.next = llist.head
    if llist.detectCycle():
        print("..Yay! cycle exists")
    else:
        print("Nay! :(")
