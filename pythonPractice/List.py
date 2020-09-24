## Creating list in Python ##

list1 =list()  # creating an empty list
print(list)

list2= list([20,25])  # creating a list with elements
print(list2)

list3= list(["tom", "venki", "name"])  # creating a list with strings
print(list3)

list4= list("python")
print(list4)

# List index

list5 =list([1,2,3,4,5,6])
print([list5[1:3]])
print([list5[1:]])
print([list5[3]])

# List Common operations

list1 = [2,2,4,1,32]
print(2 in list1)  # True
print(33 not in list1)  # True
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

## List slicing ## -- Slice

list =[11,22,44,788,1,8]
print(list[0:5])
print(list[:3])
print(list[2:])

## + and * operators in list  ---> + operators join the two list
 ## * operator replicates the element in the list

list1=[11,33]
list2= [1,9]
list3=list1+list2
print(list3)

list4=[1,2,3,4]
list5=list4*3
print(list5)

## Traversing list using for loop ---> we can use for loop to through all the elements of the list

list =[1,2,3,4,5]
for i in list:
    print(i,end=" ")

## Commonly used list method with return type

list1 = [2,3,4,5,6,7,3,]
list1.append(8)
print(list1)

print(list1.count(3))

list2=[10,11]
list1.extend(list2)
print(list1)

print(list1.index(4))

list1.insert(1,25)
print(list1)

list1=[1,2,3,4,5,6,7,8,9]
print(list1.pop(2))
print(list1)

list1.remove(7)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

## List Comprehension ###

list1= [x for x in range (10)]
print(list1)

list2=[x+ 1 for x in range (10)]
print(list2)

list3=[x for x in range (10) if x % 2==0]
print(list3)










