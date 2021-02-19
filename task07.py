
#Convert temperature from celsius to Fahrenheit
def convertCelsius(celsius):
    f = (celsius * 1.8)+32
    return f

celsius = input("Enter a temperature in celsius ")
celsius = float( celsius )
# Pass our temperature variable to the function
print(convertCelsius(celsius))
f = convertCelsius( celsius )
print('The temperature in Fahrenheit is: ', f)

#convert temperature from Fahrenheit to celsius
def convertFahrenheit(Fahrenheit):
    c = (Fahrenheit - 32)/1.8 
    return c

Fahrenheit = input("Enter a temperature in Fahrenheit: ")
Fahrenheit = float( Fahrenheit )

print(convertFahrenheit(Fahrenheit))
c = convertFahrenheit( Fahrenheit )
print('The temperature in celsius is: ', c)


