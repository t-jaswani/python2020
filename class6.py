class REC():
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def rarea(self):
        ra = l*b
        return ra
    def rperimeter(self):
        rp = 2*(l+b)
        return rp

    result = REC(6,7)   
    print(result.rarea(), result.rperimeter()) 




