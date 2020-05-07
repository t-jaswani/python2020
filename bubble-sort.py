
list1 = [4,3,2,7,9,11,1,16]
z = list1[0]
print(z)

def bubble(list3):
    list2 = []
    for x in list3:
        print("The value of x is:", x)
        count = 1
        temp = 0

        while count<len(list3):
            if list3[count] < x:
                temp = x
                print("The value being compared to x:", list3[count])
                x = list3[count]
            count+=1
            list2.append(x)
            list3.pop(x)
    return list2        

y = bubble(list1)
print(y)

""""
1. create a function 
2. Keep tally from last position to first position - create a separate list to put in the filtered items
3.Add functionality to shift items from pivot either to the left or right depending on size 
i)  how to shift the items? - len
ii) how to choose the pivot?
iii) checking the size!!

4. return a sorted list 

- Setting up their machine for development """


 