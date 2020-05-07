x = [23,34,1,5,8,67,7,54]


"""
#def mergesort(list1):
1. divide the list into 2 
2. check if the list has more than 1 item 
3. Join the list together while sorting
"""
x = [23,34,1,5,8,67,7,54]

def MergeSort(x):
    print("The value os x is: ", x)
    print("the tyoe of x is: ", type(x))
    firstHalf =[]
    secondHalf = []
    ##w = []

    if len(x) > 1:
        pivot =int(len(x)/2)
        firstHalf = x[:pivot]
        secondHalf = x[pivot:]
        #print("The value of w is: ", w)
    w = MergeSort(firstHalf) + MergeSort(secondHalf)
        #print("The value of w is: ", w)
    count = len(w)
    while count>=1:
        if w[count]<w[count-1]:
            w.insert(count-1,w[count])
            w.pop()
            count-=1
    return w

"""
        print("the value of w",w)
    count = len(w)
    while count>=1:
        if w[count]<w[count-1]:
            w.insert(count-1,w[count])
            w.pop()
            count-=1
    """

print(MergeSort(x))    

"""        
w = [7,5]
if w[1]<w[0]:
    w.insert(0,w[1])
    w.pop()
print(w)

while count < pivot:
    firstHalf.append(x[count])
    secondHalf.append(x[-count-1])
    count+=1
#print(firstHalf)   
#print(secondHalf)"""