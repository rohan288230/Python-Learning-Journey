#Temperature Converter
cel_temp = int(input("Enter temperature in celcius : "))
fahr_temp = (cel_temp * 9 / 5) + 32
kel_temp = cel_temp + 273.15
print("The temperature in Fahrenheit is : ",fahr_temp)
print("The temperature in Kelvin is : ",kel_temp)