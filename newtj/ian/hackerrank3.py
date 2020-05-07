def sort1(list1):
    # list1.sort()
    # y = []
    # for x in list1:
    #     y.append(x[1])
    # f = list(dict.fromkeys(y))
    # f.sort()
    # z = f[1] 
    # for x in list1:
    #     if x[1] == z:
    #         print(x[0])  
    
    return list1




if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data = [name,score]
        list1.append(data)
    sort1(list1)