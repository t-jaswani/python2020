import numpy as np

# 0 dimensional array
x = np.array(0)
print("O dimensional array",x)

# 1 dimensional array
y = np.array([0,1,4,3,4,5,6])

print("One dimensional array",y)

# 2 dimensional array
z = np.array([[2,3,4,5],[2,3,4,5]])
print("A two dimensional array: ", z)
print("ndim command to print the dimentions",z.ndim)#ndim command page 186

# 3 dimensional array
a = np.array([[[1,2,3,4],[5,6,7,8]],[[9,8,7,6],[5,4,3,2]]])
print("A three dimensional array: ", a)

#print what is in position 2
print("The item in position 2 is: ",y[2])

#accessing certain items
print(y[1:4])

#z = np.array([[2,3,4,5],[2,3,4,5,6]])
#accessing items from 2d
z = np.array([[2,3,4,5],[2,3,4,5]])
print("The 2D array is: ", z[0:1]) 

p = np.arange(0,10,5)
print("Creating an array using linspace",p)