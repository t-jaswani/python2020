#Write a python function to find the max of three numbers.

def m1(l):
    d = max(l)
    return d

l = [1,2,3,4,5]
print(m1(l))


#Write a python function to sum up all the items in a list
def s1(s):
    e = sum(s)
    return e
s = [1,2,3,4,5]
print(s1(s))


#multiply all the items in a list

import math
def mul1(x):
    f = math.prod(x)
    return f
x = [1,2,3,4]
print(mul1(x))

#function that checks whether a passed string is palindrome
def str4(str1):
    str2 = ''.join(reversed(str1))
    if str1 == str2:
        return 'yes'
    else:
        return 'no' 
str1 = 'racecar' 
print(str4(str1))         

#string is a pangram
def str6(str3):
    alphabet = ["a","b","c","d"]
    value = True
    for x in alphabet:
        if x not in str3:
            value = False
    return value
str3 = "The quick brown fox jumps over the lazy dog"
print(str6(str3))

#Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)

def mk():
    k = []
    n = 1
    while n < 30:
        k.append(n)
        n+=1
    return k    
def squ():
    z = mk()
    d2 = []
    for y in z:
        d1 = pow(y,2)
        d2.append(d1)
    return d2    
print(squ())

#Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.



def make_bold(fn):
    def wrapped():
        return "<b>" +fn() + "</b>"

    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" +fn() + "</i>"

    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" +fn() + "</u>"

    return wrapped

@make_bold
@make_italic
@make_underline
def name():
    return "Hello World"

print(name())

#jinja templating python(flask, django)
