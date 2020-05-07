
import random

def quickSort(array):
    """Sort the array by using quicksort."""
    print("The new array is: ", array)
    
    
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        #r = random.randint(0,len(array))
        #import pdb; pdb.set_trace()
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        print("less than =", less)
        print("Greater than =", greater)
        return  quickSort(greater) + equal + quickSort(less)
    else: 
        return array


list1 =[34,45,12,3,8,1,76,89,45,67,63,24]
print(quickSort(list1))

#pdb = imbuilt python debugger.

#concatination
'''
x = 54
y =87
z = x+y
print(z)

a = "Hello"
b = "world"
c = a + '\n' + b
print(c)

t = ["cars","toyota","mercedecies"]
s = ["toys","food","country"]
v = t + s
print(v)
'''