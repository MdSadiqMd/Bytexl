<<<<<<< HEAD
def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=[5,3,8,6,7,2]
print("The Unsorted List is:",list1)
=======
def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=[5,3,8,6,7,2]
print("The Unsorted List is:",list1)
>>>>>>> 6d4c0bdaf237af1555cf484289d2fa8b6668d854
print("The sorted list is:",bubble_sort(list1))