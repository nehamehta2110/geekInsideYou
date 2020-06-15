#rotate an array arr[] of size n by d elements


def arrRot(arr,n,d):
    for i in range(d):
        arrRotateByOne(arr,n)

def arrRotateByOne(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]= arr[i+1]
    arr[n-1]=temp

def arrRet(arr,n):
    for i in range(n):
        print('%d'%arr[i],end=',')

arr=[1,2,3,4,5,6,7,8]
arrRot(arr,len(arr),2)
arrRet(arr,len(arr))