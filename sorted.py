# #sorted, read up on key!!... Write 10 different examples on sorted
#sorted(iterable, key=key, reverse=reverse)
# The value of the key parameter should be a function that takes a single argument and returns
# a key to use for sorting purposes. This technique is fast because the key function is called 
# exactly once for each input record.
# list1 = [3,4,2,6,8,1,5,2] 
# a=list1.sort()
# #b = sorted(list1)
# print(list1.sort())
#
# #print(list1.count(2))
# #print(sorted(list1))
#sorted(iterable, key=key, reverse=reverse)

#1
a = ["b", "g", "A", "D", "f", "c", "h", "e"]
print(sorted(a))
x = sorted(a,reverse=True,key=str.lower)
print("x is",x)
#2
#f = []
# def car(list1):
#     f=[]
#     for i in list1:
#         f.append(i[2])
#         return (f)
#print(car(car_name))
#sortbyprice = sorted(car_name,key=lambda car_name: car[2])


#1 sorting dictinary and tupples with ittemgetter
from operator import itemgetter
car_name = [("BMW",1990,500000),("Merc",2005,1000000),("Jaguar",2015,3000000),("Audi",2020,6726000)]
sortbyprice = sorted(car_name, key= itemgetter(1), reverse=True) #sorting using itemgetter
print("sortbyprice-tup---->",sortbyprice)
#2
car_name_dict = {"bmw":[1990,50000], "Merc":[2005,100000], "Jaguar":[2015,3000000], "Audi": [2020,67260000]}
sortbyprice1 = sorted(car_name_dict.items(),key = itemgetter(1), reverse=True)
print("sortbyprice-dict-otput tupp-->",sortbyprice1)
sortbyprice2 = dict(sorted(car_name_dict.items(),key = itemgetter(1), reverse=True))
print("sortbyprice-dict-->",sortbyprice2)

#3 using lamanads
# sortbyprice = dict(sorted(car_name.items(), key=lambda item: item[1], reverse=False)) #sorting the dict by values
# print(sortbyprice)
#4
list3 = [3,4,8,1,3,7,9,11]
def sq(x):
    return x**2

print(sorted(list(map(sq,list3))))
# inventory = {2:'banana', 3:'apple', 1:'orange', 5:'pear', 4:'mangos'}
# print(dict(sorted(inventory.items())))
print(sorted(list3))