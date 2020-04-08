list1 = [4,3,2,7,9,11,1,16]

def bubble(nlist):
    for x in range(len(nlist)-1,0,-1):
        print("The value of x is: ", x)
        for i in range(x):
            print("The value of i is: ", i)
            if nlist[i] > nlist[i+1]: 
                print("---->", nlist[i])
                print("------------->",nlist[i+1])
                print("Currently the list is:", nlist)
                temp = nlist[i] 
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


bubble(list1)
print(list1)
"""
lists - manipulating lists 
- multiple ways to get items from a list """