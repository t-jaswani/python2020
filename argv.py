def example(*args,**kwargs):
    print("args -", args)
    print("Kwargs ->", kwargs)

example("lion",2,3,4,5,6,"we","are","healthy", name="tarun",country="India")

def solution(*args):
    w =[]
    for x in args:
        w.append(x)
    
    return w

print(solution("phone","android","ios",'tablet',"laptop","random"))

def solution2(**kwargs):
    take1 = []
    take2= kwargs["phone2"]
    print("take 2 ---------------->",take2)
    #print(type(take1))


solution2(phone="Nokia, samsung",phone2="Iphone",laptop="Mac",laptop2="hp",)