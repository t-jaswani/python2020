"""
Create a variable X and set it equal to a List
Create a variable Y and set it equal to an empty tuple
"""
x = [] #empty lits
y = ()# truple
"""
What is int, float, string, dictionary
"""

x = {"b":2,"a":4,"c":8,"d":7}
print(type(x))

q =  lambda a,b : a*b
print(q(5,7))

"""
- create a range from 0 to 100 skipping/multiples of 5
"""
r  = range(0,100,5)
print(r)
for i in r:
    print(i)
"""
- create a function that  takes one parameter and mutiples it by pie(22/7)
"""
def parameter(p):
    k = (p*22)/7
    return k
   
print(parameter(7))

"""
- Create a class called employee that should be initialised with two parameters, name and age
- Add a method to add name
- Add another method to add age
- Add a method to delete age
- Create two employees X and Y
- Add L name to be Mary and Y name to be Jane
- Add M age to be 23 and Y age to be 43
"""


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def addname(self,name):
        self.name = name
        return self.name

    def getname(self):
        return self.name

    def addage(self,age):
        self.age = age 
        return self.age

    def getage(self):
        return self.age
        
L = employee("mary",23)
M = employee("June",43)

print(L.getname())
L.addname("Another Mary")
print(L.getname())
    

