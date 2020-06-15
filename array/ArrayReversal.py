def arrayReversal(arr,n):
    start = 0
    end = n-1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    print(arr)

arr=[1,2,3,4,5,6,7]
n=len(arr)
arrayReversal(arr,n)