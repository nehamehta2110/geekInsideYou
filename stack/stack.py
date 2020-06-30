from sys import maxsize


def createStack():
    """"
    function to create stack
    """
    stack = []
    return stack


def isEmpty(stack):
    """flag to check if stack is empty"""
    return len(stack) == 0


def push(stack, element):
    """
    inserts element in stack
    """
    stack.append(element)
    print("-- element: {} pushed into stack!".format(element))


def pop(stack):
    """
    removes element from stack in reverse order of insertion (LIFO or FILO)
    """
    if isEmpty(stack):
        print("-- element cannot be popped, empty stack!")
        return str(-maxsize - 1)
    print("-- element: {} popped from stack!".format(stack.pop()))


def peek(stack):
    """
    returns top element of stack
    """
    if isEmpty(stack):
        print("-- empty stack!")
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


def main():
    """execution begins here"""
    stack = createStack()
    push(stack, 3)
    push(stack, 4)
    push(stack, 5)
    pop(stack)
    print(peek(stack))


if __name__ == '__main__':
    main()
