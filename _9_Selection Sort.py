def selection_sort(array):
    length=len(array)
    for i in range(length-1):
        minIndex=i
        for j in range(i+1,length):
            if array[j]<array[minIndex]:
                minIndex=j 
        array[i],array[minIndex]=array[minIndex],array[i]
    return array
array=[5,3,8,6,7,2]
print("The Unsorted List is:",array)
print("The sorted list is:",selection_sort(array))