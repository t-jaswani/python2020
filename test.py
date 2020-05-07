#Python program to convert a tuple to a string.
name = ("Brian","54","purity")

number = 54
another = str(number)
print(type(another))

string = "".join(name)
print(string)

string = " ".join(name)
print(string)

#Python program to convert a list to a tuple.
answer =[4,6,57,"yes","No"]
final = tuple(answer)
print(type(final))

#program to remove an item from a tuple.

a = list(answer)
#now remove from the list, kind of cheat 

#Python program to unzip a list of tuples into individual lists.

t = (7,5,78,90,12)
c = list(t)

for q in c:
    s =[q]

    print(s)