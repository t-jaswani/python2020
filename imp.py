# x = heapq.nsmallest(4,list1)
# y = heapq.nlargest(3,list1)
# list(heapq.merge(x,y))
# ----------
# #sorting a dict with keys/value using itemgetter
# from  operator import itemgetter
# inventory = {2:'banana', 3:'apple', 1:'orange', 5:'pear', 4:'mangos'}
# print(sorted(inventory.items(), key=itemgetter(0)))# 0 if by keys, 1 if by values
# print(sorted(inventory,key=itemgetter(0),reverse=True))
# #sorting with values using lambda
# print(dict(sorted(inventory.items())))#sorting with keys
# sortbyprice = dict(sorted(car_name.items(), key=lambda item: item[1], reverse=False)) #soring with values using lambda
# --------------------------
#map and lambda work in opposite ways, may will have function first andt hen parameters, while its the opposite in case of lamda
#result = list(map(lambda x: x*x, numbers))
#dictionary
# 1) d.fronkeys(k,[v])--new dictionary with keys with sequnce k and value all set to v
# 2) page 324 d.get(),d.items(),d.keys(),d.values(),d.pop(k,[v])
#list
# 1) page 293 sum(list), list.index(x),list.extend(list1), list.count(x), list.remove(x), list.pop(),
# list.sort(), list.pop(), list.reverse()
# tuples - data cannpt be modified - added, removed or edited..they are just used to retreive the data that has 
#to remain unchnaged after creation ..min(tpl),max(tpl),tpl.count(x), sorted(tpl)..pg 312
#sets - order is not maintaind, {10,20,40}--it does't store any repetions..page 61..
#range - list(range(10)), for i in range(30,40,2)
#arrays page160
# numpy -  A) import numpy as np, a = np.array([2,3,4,5]), p = np.arange(0,10,5),print("find dimention of an arrays",z.ndim)
#          B) a3=np.ones(10)*5,a3+2,a3*2,np.matrix(a8),arr2.nbytes
#page175,160 C) b = np.reshape(a,(2-rows,5-col)), print("this will print number of rows",len(b)),
#          print("this will priint elemnt at row 0 and col 0",b[0][0]), print("this will print complete row1",b[1])
#         f = np.ones((2,5),float)*5,g = np.eye(3,dtype=float)
#        D)rand_num1 = np.random.rand(27),c = np.reshape(rand_num1,(3,3,3)), b = rand_num1.reshape(3,3,3),x= np.random.rand(27) OR x = np.random.random((3,3,3))
#        print(x.max(),x.min(),x.mean(),x.sum(),x,prod()),print("sum of each column",x.sum(0)), print("sum of each row",x.sum(1))
#        E) reshape(a1,(n,r,c))-page 191, a = np.matrix(arr), p = y.flatten(),dia = np.diagonal(e),np.transpose(s1)
#        s = np.sort(e)-"row wise", s1= np.sort(e,axis=0)-col wsie, m1 = np.matrix('1 2 3;4 5 7;7 8 9') --we can add,*,/ matrices
#        G) ran = np.random.rand(12) --random numbers,x = np.random.randint(low=10, high=30, size=6),x = np.random.random((3,3,3))

#       --------------------------Panadas----   
# Pandas = Import panadas as pd , pandas is all about df(dataframe)
# filename = "avocado.csv" or "avocado.txt"
#df = pd.read_csv(filename)
#df = pd.DataFrame(
# 	[['Jan',58,42,74,22,2.95],
# 	['Feb',61,45,78,26,3.02],..
# df.index,df.column,df.values,df.column_name,sum(df.column_name),df.plot(),
# df["AveragePrice"].head(10), 
# albany_df = df[ df['region'] == "Albany"]
# albany_df.head()
# albany_df.tail()
# albany_df.plot()
# albany_df.index
# albany_df.columns
# albany_df.values()
# albany_df["AveragePrice"].values()
# albany_df.set_index("Date",inplace = True)  
# albany_df["AveragePrice"].plot()  
# albany_df["AveragePrice"].sum()
# albany_df["AveragePrice"].head(10)
# albany_df["region"].unique()

# https://colab.research.google.com/drive/1wJ_TF-RWkqUpZ1xbvEZB9wyU23n-tHye#scrollTo=YzOSFvy6Yphu
#https://www.w3resource.com/python-exercises/

#          B) a3=np.ones(10)*5,a3+2,a3*2,np.matrix(a8),arr2.nbytes
#page175,160 C) b = np.reshape(a,(2-rows,5-col)), print("this will print number of rows",len(b)),
#          print("this will priint elemnt at row 0 and col 0",b[0][0]), print("this will print complete row1",b[1])
#         f = np.ones((2,5),,g = np.eye(3,dtype=float)
#        D)rand_num1 = np.random.rand(27),c = np.reshape(rand_num1,(3,3,3)), b = rand_num1.reshape(3,3,3),x= np.random.rand(27) OR x = np.random.random((3,3,3))
#        print(x.max(),x.min(),x.mean(),x.sum(),x,prod()),print("sum of each column",x.sum(0)), print("sum of each row",x.sum(1))
#        E) reshape(a1,(n,r,c))-page 191, a = np.matrix(arr), p = y.flatten(),dia = np.diagonal(e),np.transpose(s1)
#        s = np.sort(e)-"row wise", s1= np.sort(e,axis=0)-col wsie, m1 = np.matrix('1 2 3;4 5 7;7 8 9') --we can add,*,/ matrices
#        G) ran = np.random.rand(12) --random numbers,x = np.random.randint(low=10, high=30, size=6),x = np.random.random((3,3,3))

import numpy as np 
a3=np.array(4,2,8,1,9)

print(a3.arrange())








