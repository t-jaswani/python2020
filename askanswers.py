
class ask:
    def __init__(self, k, u):
        self.k = k
        self.u = u

w =ask(23,36)
y =ask(34,45)

print(y)
print(w.__dict__)


t = {"key":"value"}

t["ask"] = "answers"

print(t)

class Person:
    def __init__(self, id):
        self.id = id
        self.age = 49

sam = Person(100)

sam.__dict__['age'] = 49

print("The dict ---->", sam.__dict__)