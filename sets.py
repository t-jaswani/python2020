days = {"Monday", "Tuesday", "Wednesday"}

for x in days:
    print("----------------->",x)

#Add data to set
days.add("Thursday")
print(days)

#update data in set
days.update(["friday","saturday","Sunday"])
print("The days of the week are: ", days)

#Delete data in set
days.remove("Monday")
print("New days ---------------->", days)

days.discard("Tuesday")
print("Without Tuesday --------------->", days)

#how to get len 
print(len(days))

def sets(n):
    x = range(0,n+1)
    return x

print(sets(10))
 