import numpy as np 
a = np.arange(0,10)
print(a)
b = np.reshape(a,(2,5))
c = a.reshape(5,2)
print("b b b")
print(b)
print("this will print number of rows",len(b))
print("this will priint elemnt at row 1 and col 4",b[1][4])
print("this will print complete row1",b[1])
print("-------------")
print(c)
d = np.ones((2,5),float)
e = np.zeros((5,2),int)
f = np.ones((2,5))*5
g = np.eye(3,dtype=float)
print(d)
print(e)
print(f)
print(g)







