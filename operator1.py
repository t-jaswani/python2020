#https://docs.python.org/3/library/operator.html

from  operator import itemgetter
# y ="name"
# s = "date"
# x = attrgetter(y,s)
# print(x)
inventory = {2:'banana', 3:'apple', 1:'orange', 5:'pear', 4:'mangos'}
inventory1 = [(2,'banana'), (3,'apple'), (1,'orange'), (5,'pear'), (4,'mangos')]
inventory.items()
# print(inventory.items())
# print(sorted(inventory.items(), key=itemgetter(0)))
print(sorted(inventory1, key=itemgetter(1)))

#print(list(map(itemgetter(1), inventory.items)))
