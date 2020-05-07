#from numpy import *
import numpy as np

# maths function on array 
p = np.array([4,5,6,7])
print("Orignal array",p)

print("adding 5",p+5)
k = min(p)
print("mutiplying 5",p*5)

#more math function page 175

#Comparing of arrays

a1 = np.array([2,3,4,5,11,7])
a2 = np.array([3,0,2,5,9,6])
a3 = a1 == a2
a7= np.array([[2,3,4,5],[3,4,5,6]])
print("coampring",a3)
a4 = a1>a2
a5 = np.array([[[10,16,2,1],[4,5,9,1]],[[6,7,8,1],[3,7,2,1]],[[4,8,0,1],[5,2,1,1]]])
print("greater than",a4)
print("to check if any one elemnt is true as per the condition",any(a3))
print("to check if all elemnt are true as per the condition",all(a3))
print(a5)
print("ndim command to count the diemtions",a5.ndim)
print("shape is a tupple defining number of elemenst in each diemntions",a5.shape)
print("size to diplay total elements", a5.size)
print("flatten method to collapse th dimentions into one dimention",a7.flatten())
#b = random.rand()
