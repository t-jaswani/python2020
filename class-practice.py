# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
#These brackets must be close in the correct order, for example 
# "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

class validity:
    def __init__(self,str1):
        self.str1= str1.strip()
    def check(self):
        print("------------------>", self.str1)
        c = []

        i = 0
        if len(self.str1)%2==0: 
            while i < len(self.str1):
                if self.str1[i]+self.str1[i+1]=="{}" or self.str1[i]+self.str1[i+1] == "[]" or self.str1[i]+self.str1[i+1] == "()":
                    c.append(1)
                    
                else:
                    c.append(-1)  
                i+=2   
            if len(self.str1)/2>sum(c):
                print("invalid")
            else:
                print("valid")    
             
        else:
            print("invalid")    
b = validity(" [][](){}")
b.check()



 

