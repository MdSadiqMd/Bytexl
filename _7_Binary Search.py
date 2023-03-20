def BinarySearch(array,k,low,high):
    if low<high:
        return False
    else:
        mid=(low+high)/2
        if k==array[mid]:
            return mid
        elif(k>array[mid]):
            return BinarySearch(array,k,mid+1,high)
        else:
            return BinarySearch(array,k,low,mid-1)
    return -1
array=[1,3,5,7,9]
k=7
n=len(array)
print(array)
print(BinarySearch(array,k,0,n-1))