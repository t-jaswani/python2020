"""Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a
 specific target number. 
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4"""


class element:
    def calc (self, num, target):
        lookup =  {}
        for i, num in enumerate(num):
            print("the value of i is: ",i)
            print("------------------ num -->: ",num)
            if target - num in lookup:

                return(lookup[target-num],i)

            lookup[num] = i


print(element().calc((10,20,10,40,50,60,70),50))

   


    
