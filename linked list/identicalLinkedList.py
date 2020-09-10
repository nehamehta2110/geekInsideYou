# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

'''


def areIdentical(head1, head2):
    # Code here
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next

    return True


# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')
# } Driver Code Ends
