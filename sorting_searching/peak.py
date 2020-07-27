# your task is to complete this function
# function should return index to the any valid peak element


def peakElement(arr, n):
    # Code here
    if n is 1:
        return 0
    for i in range(n):

        # if element at first index is greater than next
        if i == 0 and arr[1] < arr[0]:
            return 0

        # if element is at last index and it is greater than
        # its prev one
        elif i == n - 1 and arr[n - 2] < arr[n - 1]:
            return n - 1

        # case, when element is at any other index
        # then you need to check both of its neighbour
        elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            return i


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n == 1:
            flag = True
        elif index == 0 and arr[index] >= arr[index + 1]:
            flag = True
        elif index == n - 1 and arr[index] >= arr[index - 1]:
            flag = True
        elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
            flag = True
        else:
            flag = False

        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends
