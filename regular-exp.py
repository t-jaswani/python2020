
import re
#prog = re.compile(r'c\w\w')
str = 'cake,bat,rat,5,cow,can,call,cactus,Canister,1st,234,4orty'
#result = prog.search(str)
result1 = re.search(r'c\w\w', str)#will only give first matching word
result2 = re.findall(r'c\w\w', str)
result3 = re.match(r'c\w\w', str) #only in the begening of the string
result4 = re.split(r'\W+', str)
result5 = re.sub(r'bat','BALL', str)
result6 = re.findall(r'c[\w]*', str) # all words starting with c
result7 = re.findall(r'\d[\w]*', str) # all words starting with numericals
print(result1.group())
print(result2)
print(result3)
print(result3.group())
print(result4)
print(result5)
print(result6)
print(result7)




