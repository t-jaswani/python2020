#Write a Python class to reverse a string word by word. Input string : 'hello .py'Expected Output : '.py hello'


class string1():
    def __init__(self,str1):
        self.str1 = str1

    def reverse(self):
        str2 = ' '.join(reversed(self.str1.split()))
        return str2
result1 = string1("hello World I am new")            
print(result1.reverse())            

##Write a Python program to get the class name of an instance in Python.

