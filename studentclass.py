"""Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
"""
"""
keywords:
parameter
methods
difference between functions and methods
self = represents the instance of that class

create a student mark and set his age to 20
create a student jane and set her marks as 25
 """

class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber
        self.age = int
        self.marks = int

    def display(self):
        app = [self.name, self.rollnumber]
        return app     

    def setage(self, age):
        self.age = int(age)
        return self.age

    def setmarks(self, marks):
        self.marks = int(marks)    
        return self.marks

mark = Student(mark, 15)
mark.setage(20)
jane = Student(jane, 18)
jane.setmarks(25)