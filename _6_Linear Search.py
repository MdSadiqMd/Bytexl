def LinearSearch(array,n,k):
    for j in range(0,n):
        if (array[j]==k):
            return j
    return-1
array=[1,3,5,7,9]
k=7
n=len(array)
print(LinearSearch(array,n,k ))