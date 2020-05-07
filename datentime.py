#to find secomds since 1st jan 2020
import time
epoch = time.time()
print(epoch)
#converting epoch to today's date

#currnet date and time
import time
t1 = time.ctime()
print(t1)
#write a function that displays the current time in the formart(dd/mm/yy)

from datetime import*
now = datetime.now()
print(now)
#print date and time
print(format(now.day),format(now.month),format(now.year))
tdm = datetime.today()
#print date
print(tdm)
td = date.today()
print(td)
#formatting dates
str= td.strftime("%d, %B, %Y")
print(str)



