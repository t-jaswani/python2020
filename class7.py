
class Circle():
    def __init__(self,r):
        self.r = r
        
    def area(self): 
        a = (22*(self.r**2))/7
        return a

    def perimeter(self):
        p = (2*22*self.r)/7  
        return p  

result = Circle(7)
print(result.area(), result.perimeter())

