# to search from a file 

f = open('practice.py','r')
for str in f:
    res = re.findall(regexpression,str)
print(res)