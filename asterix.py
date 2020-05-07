def example(*ite,**kw):
    print(ite,kw)

example([2,3,4,5,6])

example(2,"3",a = "another")

import operator
list1 = ["3","4","5","6","7","8","9"]
list1.operator.delitem(5,2)
print(list1)