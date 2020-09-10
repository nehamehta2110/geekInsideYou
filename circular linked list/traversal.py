class Node:

    # add code here
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):

        # add code here
        temp = Node(data)
        ptr = self.head
        temp.next = self.head
        if self.head is None:
            temp.next = temp

        else:
            while ptr.next != self.head:
                ptr = ptr.next

            ptr.next = temp

        self.head = temp

    #  Function to print nodes in a given Circular linked list
    def printList(self):

        # add code here
        if self.head is None:
            return
        print(self.head.data, end=' ')
        r = self.head.next
        while r != self.head:
            print(r.data, end=' ')
            r = r.next


# {
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        cllist = CircularLinkedList()
        l = list(map(int, input().strip().split()))
        for i in range(0, len(l)):
            cllist.push(l[i])
        cllist.printList()
        print()
# } Driver Code Ends
