"""
given arr[2,3,2,1,5] output repeating number 2 and missing number 4
count array method:
if(temp[arr[i]] == 0) temp[arr[i]] = 1;
if(temp[arr[i]] == 1) output “arr[i]” //repeating
Traverse temp[] and output the array element having value as 0 (This is the missing element)
"""


def repeat_and_miss(arr, size):
    temp = [0] * size

    print(temp)

    for i in range(size):
        if temp[arr[i] - 1] == 0:
            temp[arr[i] - 1] = 1
        else:
            print("--Repeating element is", arr[i])

    print(temp)

    for i in range(size):
        if temp[i] == 0:
            print("--Missing element is", i + 1)


arr = [7, 5, 4, 5, 3, 2, 6]
n = len(arr)
repeat_and_miss(arr, n)
