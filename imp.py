# x = heapq.nsmallest(4,list1)
# y = heapq.nlargest(3,list1)
# list(heapq.merge(x,y))
# ----------
# #sorting a dict with keys/value using itemgetter
# from  operator import itemgetter
# inventory = {2:'banana', 3:'apple', 1:'orange', 5:'pear', 4:'mangos'}
# print(sorted(inventory.items(), key=itemgetter(0)))# 0 if by keys, 1 if by values
# print(sorted(inventory1,key=itemgetter(0),reverse=True))
# #soring with values using lambda
# print(dict(sorted(inventory.items())))#sorting with keys
# sortbyprice = dict(sorted(car_name.items(), key=lambda item: item[1], reverse=False)) #soring with values using lambda
# --------------------------
#map and lambda work in opposite ways, may will have function first andt hen parameters, while its the opposite in case of lamda
#result = list(map(lambda x: x*x, numbers))

