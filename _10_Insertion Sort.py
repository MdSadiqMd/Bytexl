def Insertion_sort(list1):
    for i in range(1,len(list1)):
        key=list1[i]
        j=i-1
        while j>=0 and key<list1[j]:
            list1[j+1]=list1[j+1]
            j-=1
        list1[j+1]=key
    return list1
list1=[10,5,13,8,2]
print("The Unsorted list is:",list1)
print("The sorted list1 is:",Insertion_sort(list1))