"""Write a Python class to implement pow(x, n).
"""

class powe():
    def __init__(self,x,n):
        self.x = x
        self.n = n
 
    def pow_r(self):
        r = self.x**self.n
        return r

    
result = powe(2,4)
print(result.pow_r())