#https://www.w3resource.com/python-exercises/dictionary/
#1 Write a Python script to sort (ascending and descending) a dictionary by value
dict1 = {"a":4,"b":2,"c":3,"d":5}
 
def sort(dict1):
    a = []
    dict2 = {}
    for i in dict1:
        a.append(dict1[i])
    a.sort()  
    for i in a:
        for x in dict1:
            if i == dict1[x]:
                dict2.update({x:dict1[x]})
    #print(dict2.get("a"), dict2.keys(),dict2.values(),dict2.items())
    #print(len(dict2))
    return    

print(sort(dict1))

import heapq
def solution():
    
#2 Write a Python script to add a key to a dictionary
dict1["e"] = 7
print(dict1)
#3  Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic2.update(dic3)
dic1.update(dic2)
print(dic1)
#4 Write a Python script to check whether a given key already exists in a dictionary. 
print(dic1.get(1))
print(dic1.get(11,["false"]))
#5. Write a Python program to iterate over dictionaries using for loops.
for k in dic1:
    print("keys -->", k)
    print("values -->", dic1[k])
#6.# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 10
dictnew = {}
def newdict(n):
    for i in range(1,n):
        dictnew[i] = i*i
    return dictnew
print(newdict(n))
#7 Write a Python program to sum all the items in a dictionary.
d = sum(dic1.values())  
print(dic1,"sum of values in the dictionary-->",d)   
#8 Write a Python program to multiply all the items in a dictionary.
multi = 1
for i in dic1:
    multi = multi*dic1[i]
print(dic1,"multiplying th evalues of a dict--->", multi)
#9 Write a Python program to remove a key from a dictionary. 
print(dic1)
print(dic1.pop(6))
print(dic1.pop(11,["false"]))
#print(dic1.pop(11))

#print(dic1,dic1.pop(6),dic1,dic1.pop(11),dic1.pop(11,["false"]))
#10 #Write a Python program to map two lists into a dictionary.
dmap1 = ["r","b","g","e"]
dmap2 = [10,20,30,40]
dmap = {}
count = 0
for i in dmap1:
    dmap[i] = dmap2[count]
    count+=1
print(dmap)
#11 Write a Python program to get the maximum and minimum value in a dictionary. 
dsort = {3: 10, 2: 30, 5: 40}
list1 = []
dsort1 = []
for i in dsort:
    list1.append(dsort[i])
    list1.sort()
print("the smallest value is --->",list1[0],"the largest value is --->",list1[len(list1)-1])
# 12 # Write a Python program to combine two dictionary adding values for common keys.
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for i in d2:
    #y = d2.pop(i)
    if i in d1:
        d1[i] = d2[i] + d1[i]
    else:
        d1[i]= d2[i]    
print(d1)    
#13  Write a Python program to print all unique values in a dictionary. Go to the editor
#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

sd = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
count = 0
lfinal = []
while count<len(sd):
    d = sd[count]
    for i in d:
        if d[i] not in lfinal:
            lfinal.append(d[i])
    count+=1    
print(lfinal)
