1) class car(): vs class car: 

 2) class car(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
          
# both objects have different self which  
# contain their attributes 
audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 
  
audi.show()    car.show(audi)  # same output as car.show(audi) ?????
ferrari.show()  # same output as car.show(ferrari) ???

class Person:
    def __init__(self, id):
        self.id = id
        self.age = 49

sam = Person(100)

sam.__dict__['age'] = 49

print("The dict ---->" + sam.__dict__)

https://www.geeksforgeeks.org/self-in-python-class/
Q-10, 11, 12...