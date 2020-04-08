#Python program to create a tuple
tup = (5,6,7,8)
print(tup [-2])
#to create a tuple with different data types.
tu = (5,6, "hello", "world")
print(tu)
print("--------------")
#unpack a tuple in several variables
a ,b,c,d= tu[0:4]
print(a,b,c,d)
print("--------------")
#add an item in a tuple
tua = (1, ) #was not able to add one
print("The type is --->",type(tua))
#tua.insert("ok",0)
tup = tup + tua
print(tup)
print("--------------")
# tuple to string
#tin = s,t,r,i,n,g


# get the 4th element and 4th element from last of a tuple.
tim = 1,2,3,"ed","fg",4,9,11,8,45
print(tim[4])
print(tim[-4])
print("--------------")
#print repeated items of a tuple. 
ton = 2,3,4,5,3,6,2,3,4,1
store =[]
for x in ton:
    if ton.count(x)>1:
        store.append(x)

print(store)
store = list(dict.fromkeys(store))# Ian needs to make me understand this 
print("Store ----------------->",store)
        #ton.remove(x)
# check whether an element exists within a tuple.
toy = 4,5,3,2
print(toy.index(4))
print("--------------")
#Python program to convert a tuple to a string.
name = ("Brian","54","purity")

number = 54
another = str(number)
print(type(another))

string = "".join(name)
print(string)

string = " ".join(name)
print(string)
print("--------------")

#Python program to convert a list to a tuple.
answer =[4,6,57,"yes","No"]
final = tuple(answer)
print(type(final))
print("--------------")
#program to remove an item from a tuple.

a = list(answer)
#now remove from the list, kind of cheat 
print("--------------")
#Python program to unzip a list of tuples into individual lists.

t = (7,5,78,90,12)
c = list(t)

for q in c:
    s =[q]

    print(s)