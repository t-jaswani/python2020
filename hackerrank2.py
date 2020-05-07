def runnerup(arr1):
    i = int(arr1[0])
    #i = None
    for x in arr1:
        if int(x) > int(i):
            i = x
    arr1.remove(i)
    
    i = arr1[0]
    for x in arr1:
        if int(x) > int(i):
            i = x
            return i     
        


if __name__ == '__main__':
    n = int(input())
    arr1 = []
    i = 0
    while i <n:
        k = input()
        arr1.append(k)
        i+=1
    print(arr1)
    #arr1 = map(input().split())
   
    print(runnerup(arr1))
    
