# class Sales:
#     def __init__(self, id):
#         self.id = id
#         id = 100
#         print(id)
# val = Sales(123)
# print (val.id)

class Person:
    def __init__(self, id):
        self.id = id
        self.age= 49
class another():
    def __init__(self):
        Person.__init__(self,id)