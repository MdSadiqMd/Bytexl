<<<<<<< HEAD
#The partition block is to keep spaces in sorting the array of elements
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
arr=[2,5,3,8,6,5,4,7]
n=len(arr)
quick_sort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
=======
#The partition block is to keep spaces in sorting the array of elements
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
arr=[2,5,3,8,6,5,4,7]
n=len(arr)
quick_sort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
>>>>>>> 6d4c0bdaf237af1555cf484289d2fa8b6668d854
    print(arr[i],end=" ")