# Write a Python program to sort a dictionary by key.
# dsort = {3: 10, 2: 30, 5: 40}
# list1 = []
# dsort1 = []
# for i in dsort:
#     list1.append(i)
#     list1.sort()
# count = 0
# while count < len(list1):
#     y = dsort.get(list1[count])
#     print(y,list1[count])
#     dsort1[list1[count]] = y
#     count+=1   
# print(dsort1) 



#Write a Python program to get a dictionary from an object's fields. 

# Write a Python program to remove duplicates from Dictionary.
# dup = {3: 10, 2: 30, 5: 40, 3:20, 2:30}
# # nodup = {}
# # for i in dup:
# #     nodup[i] = dup.get(i)
# #     dup.pop(i)
# # print(nodup)
# #print(dup.pop(3))
# print(dup)
# dup1 = dup
# print(dup1)
#2 f = list(dict.fromkeys(r,1))
#1 Write a Python script to sort (ascending and descending) a dictionary by value
dict1 = {"a":4,"b":2,"c":3,"d":5}
 
# def sort(dict1):
#     a = []
#     dict2 = {}
#     for i in dict1:
#         a.append(dict1[i])
#     a.sort()  
#     for i in a:
#         for x in dict1:
#             if i == dict1[x]:
#                 dict2.update({x:dict1[x]})
#     #print(dict2.get("a"), dict2.keys(),dict2.values(),dict2.items())
#     #print(len(dict2))
#     return  dict2  

# print(sort(dict1))

# import operator
# answer = dict(sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
# print(answer)

#Write a Python script to add a key to a dictionary.

dict2 = {"b":4,"a":2,"c":3,"d":5}
# dict1["c"]= 99

# def add(dict1,key_data,value_data):
#     dict1[key_data] = value_data
#     return dict1

# print(add(dict1,"e",6))

list1=[3,43,78,5,4,23,34,67]

def another1():
    pass

t =dict(sorted(dict1.items(), key=another1() reverse=True))
#t =sorted(dict1, reverse=True)
#t =dict(sorted(dict1.items(), reverse=True))
print(t)
