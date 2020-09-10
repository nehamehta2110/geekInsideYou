# your task is to complete this function
# function should return true/1 if length is even
# else return false/0
def isLengthEvenOrOdd(head):
    # Code here
    temp = head
    c = 0
    while temp:
        temp = temp.next
        c += 1
    if c % 2 == 0:
        return True
    return False


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
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


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
        head = createList(arr, n)
        if (isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
