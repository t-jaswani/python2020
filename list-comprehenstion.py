x = [2,3,4]
y = [4,5,6]
#
# d = list(r*2 for r in x if r%2==0)
# print(d)

# u = list(i+s for i in x for s in y)
# print(u)

# k = []
# for i in x:
#     for s in y:
#         k.append(i+s)
        
#print(k)
d = list(r*2 for r in x if r>0 and r<3)
#In a list if the element lies between 0 and three, mutiply it bt 2 and store in another list. 
print(d)

#store the multiples of 5 from 0 to 100 in a list
print(list(map(int,i)) for i in range (0,100,5))