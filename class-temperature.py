"""Create a Temperature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""

class Temperature:
    def __init__(self,temp):
        self.temp = temp

    def convertCelsius(self):
        F = (self.temp*9)/5 + 32
        return F

    def convertFahrenheit(self):
        C = (self.temp-5)*5/9
        return C
    
TC = Temperature(50)
TF = Temperature(75)
#difference between printing TF.convertFahrenheit and TF.convertFahrenheit()
print("Temperature in Celcius is", TF.convertFahrenheit()) 
#print("Temperature in Fahrenheit is", TC.convertCelsius())