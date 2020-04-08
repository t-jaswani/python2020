
# import heapq
# def answer(item):
#     x = heapq.nlargest(item,10)
#     x = list(dict.fromkeys(x))
#     return x[1]

# r = [5,6,6,3,7,5,5,1,6,7,4,5,6,7,8,9]
# #f = list(dict.fromkeys(r,1))

# #f = list(dict.fromkeys(r))
# #print(f)
# #print(answer(r))    



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(answer(arr))   
import os
import heapq
#import hackerraank3
#from newtj.ian.hackerrank3 import sort1
list1 = [1,42,53,64,5,76,7,8,9]

#https://docs.python.org/3.0/library/heapq.html
#p = sort1(list1)
#print(p)
x = heapq.nsmallest(4,list1)
print(x)
y = heapq.nlargest(3,list1)
print(y)
print(list(heapq.merge(x,y)))
print(heapq.nsmallest(2,list(heapq.merge(x,y))))


