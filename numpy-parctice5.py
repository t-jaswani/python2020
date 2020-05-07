#https://www.w3resource.com/python-exercises/numpy/basic/index.php
# Write a NumPy program to create a 3x3x3 array filled with arbitrary values
import numpy as np

rand_num1 = np.random.rand(27)
# print(rand_num1)
c = np.reshape(rand_num1,(3,3,3))
#b = rand_num1.reshape(3,3,3)
#print(b)
print("printing c",c)

import numpy as np
x = np.random.random((3, 3, 3))
print("printing x",x)
big = x.max()#largest value
small= x.min()#min value
print("big---",big)
print("Small---",small)

#Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array
print(x.sum(),x.mean(),x.prod())
print("sum of each column",x.sum(0))#sum of each column
print("sum of each row",x.sum(1))#sum of each row
