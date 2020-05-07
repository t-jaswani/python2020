list1 = [1,2,3,2,4,3,6,3,7,3,9,5,3,22]
print(list1.index(3))#returns the location of first occurance in the list
y = sum(list1)
print("sum of the list", y)
list1.append(14)
print("the count of 3 is " , list1.count(3))
list1.remove(3)#removed first occurancee of 3
print("list after removing 3", list1)
list1.insert(3,0)
l2 = list1.copy()

list1.sort()
print("sorting the list", list1)

list1.reverse()
print("Reversing the list", list1)
l3 = list1
l2.extend(l3)
print(list1)
print(l2)
print(l3)

heapq




