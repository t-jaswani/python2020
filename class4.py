"""Write a Python class named Circle constructed by a radius and two methods which will compute 
the area and the perimeter of a circle.
"""

class Circle():
    def __init__(self,r):
        self.r = r
        k = self.r*5
        
    def area(self): 
        a = (22*(self.r**2))/7
        return a

    def perimeter(self):
        p = (2*22*self.r)/7  
        return p  

result = Circle(7)
print(result.area(), result.perimeter())


