def count(head, search_for):
    # Code here
    current = head
    count = 0
    while current is not None:
        if current.data == search_for:
            count += 1
        current = current.next
    return count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        m = int(input())
        k = count(llist.head, m)
        print(k)
        t -= 1
