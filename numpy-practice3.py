#Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

import numpy as np
a1=np.zeros(10)
a2=np.ones(10)
a3=np.ones(10)*5
print("a2+a3",a2+a3)
print("an array of 10 zeros, 10 ones, 10 fives-->",a1,a2,a3)
print(a1.itemsize*a1.size,"bytes")

#Write a NumPy program to create an array of even integers from 30 to70.
a5=np.arange(30,71,2)
print("Array of even integers from 30 to70")
print(a5)
print("Using linspace to create an array between 1 and 10 , equally divided")
a6 = np.linspace(1,10,5)
print(a6)
print("Using logspace to create an array between 10 ^1 to 10^4 , equally divided")
a7 = np.logspace(1,4,5)
print(a7)
#Write a NumPy program to create a 3x3 identity matrix
a8 = np.array([[2,3,4],[5,6,7],[8,2,7]])
a9 = np.matrix(a8)
print(a9)
#random arrays
import numpy as np
rand_num = np.random.rand(5)
print("Random arrays:")
print(rand_num)
#ramd arrays 2
import numpy as np
rand_num1 = np.random.normal(0,1,(2,1,2))
print("Random arrays normal:")
#bytes occupied by an array, each element occupies 8 bytes, so memory size in bytes will be 8 *number of elememst
print(rand_num1)
arr1 = np.array([[1,2,3],[7,8,6]])
print(arr1.nbytes)
arr2 = np.array([1,5,6,9])
print(arr2.nbytes)
print("-------------------------------------")
import numpy as np
rand_num = np.random.normal(0,2,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)

import numpy as np
rand_num1 = np.random.rand(15)
print("15 random numbers from a standard random distribution:")
print(rand_num1)