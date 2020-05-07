def Solution(list1,n):

    
    for x in list1:
        list2 = []
        i = 0
        while i<len(list1):
            #print("the value of i is ", x,list1[i])
            if int(x) + int(list1[i]) == int(n):
                
                list2.append(x)
                list2.append(list1[i])
                print(list2)
                list1.remove(x)
            i+=1    
    #print(list2)
if __name__ == "__main__":
    Solution([2,4,5,6,3],9)              