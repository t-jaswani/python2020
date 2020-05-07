#Create a Circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self,radius):
        self.radius= radius

    def getArea(self):
        area = (22*self.radius**2)/7
        return area    

    def getCircumference(self):
        circumderence = (2*22*self.radius)/7    
        return circumderence
C = Circle(7) 
print(C.getArea(),C.getCircumference())   

