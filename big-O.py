Big O notation
- time - checks the time an algorithm will take from start to finish
- Space - checks on how effecient the algorithm is using Space
- Bog O notation helps us to decide if the given soluton is scalable/selctable for our site
-Big O is the anlaysis of algorithm's efficeency 
-this efficeency is in terms of input size or N
https://www.youtube.com/watch?v=__vX2sjlpXU
https://www.youtube.com/watch?v=-Eiw_-v__Vo



N And Its Value in order of increasint time complexity ir Big O

A) Sattic Big(O) = 1 ..where output is independent of the input Value 
eg x = 5 +4
B) Binary  
log n       
This is one when you are able to rule out 50% of instances ..divdie and conquer

eg 
if x < 0: (O(1))
    print(x)
    else:
        if x>0 (O(logN))
    else:
        pass (O(N^2))    
the big O of the above will be O + OLogN + O(N^2) ...for a very large N we ingrore the constans so bigO will be N2
C)Linear time 
Big(O) = n..wherethe time taken is directly protional to the input, in case of lare inputs genrally constans are doppped
eg 
for x in range (0,n):
    print(n)# O(1) X N times = N
 
D) Qadratic time
for x in range (0,n): n
    for y in range (0,n):
        print(y)

the big O of the above will be O + OLogN + O(N^2) ...for a very large N we ingrore the constans so bigO will be N2
()
x = [1,2,3,4,5]
  1     2     3     4         5       6
O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(infinity)
 eg of 4 is deck of cards
    5 checking list with grocerry list
    6 flipping the coin till comes to 0

if 4 == x:
    #print("four is present")
    break

o(n)

x = i for i in x
