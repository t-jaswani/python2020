"""from breaky import boolean_details

if boolean_details(7) ==True:
    print("The value is 4")
else:
    print("The value is not 4")

#age, sex, height
"""
class Person():
    def __init__(self, age, sex,height):
        self.age = age
        self.sex = sex
        self.height = height
        self.work = None

    def add_age(self, new_age):
        self.age = new_age
        return self.age

    def add_job(self, work):
       self.work = work
       return work




ken = Person(12,"male",24)
lilian = Person(20,"Female",25)

print("Ken age : ",type(ken.age))
print("Lilian age: ",lilian.age)

ken.add_age(13)
print("New ken age: ", ken.age)

lilian.add_job("carpenter")
print("Lilian new job", lilian.work)

difference =ken.age + lilian.age
print(difference)
"""
q = [1,2,3,4,5,6,7,8]

print("The value is: ",q[7]) o(1)

for x in q:
    if x == 8:
        for c in w:
        print("The value is: ", x)
        break
    O(n**2)
    """