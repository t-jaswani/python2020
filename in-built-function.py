#Python ascii()
# Python getattr()
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)

#Python hasattr()
class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))

#input from a user
inputString = input('Enter a string:')
print('The inputted string is:', inputString)


