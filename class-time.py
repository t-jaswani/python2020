"""Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute
"""
import datetime as dt

class time:
    def __init__(self,hours,min):
        self.hours = hours
        self.min  = min

    def displaytime(self):
        print (self.hours, self.min)

    def Totaltime(self):
        t = self.hours*60 + self.min
        return t 

def add_time(time1, time2):
    x = str(time1)
    time1_hour = x[0:2]
    time1_minute = x[3:5]
    print("------------------",time1_hour)
    print("-----m---",time1_minute)

    y = str(time2)
    time2_hour = y[0:1]
    time2_minute = y[3:5]

    add1 = dt.timedelta(hours=int(time1_hour), minutes=int(time1_minute))
    add2 = dt.timedelta(hours=int(time2_hour), minutes=int(time2_minute))

    t3 = add1 +add2
    return t3

print("final :",add_time("10:32","11:50")

    
# t1 = time(12,30)
# t2 = time(5,15)
# #method displayTime which should print the time.
# t1.displaytime()
# t2.displaytime()
# #Make a method DisplayMinute which should display the total minutes in the Time
# print(t1.Totaltime()