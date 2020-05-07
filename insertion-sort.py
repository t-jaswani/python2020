#https://www.youtube.com/watch?v=JU767SDMDvA
#we start from left to right
#Each element is comapred to the item on the left and sorted untill it reaches its corrrect place. 
# 68594381
# 1) Find the element next to the top of the stack or array[1]
# 2) Compare to element on the left and the smaller one is move to top of the stack
# 3) Write a loop to do this for each element untill each postion reaches its right postion



list1 = [6,8,5,9,-2,4,3,12,8,1]

def InsertionSort(list1):
    count = 0
    marker = 1
    while marker<len(list1):
        count = marker
        while count>0:
            if list1[count]<list1[count-1]:
                x=list1[count-1]
                list1[count-1]=list1[count]
                list1[count]=x
            count-=1 
        marker+=1
    return list1  
print(InsertionSort(list1))   
