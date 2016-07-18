# input of temperature in Fahrenheit
tempF = input('What is the temperature [F]? ')
# the formula for conversion
tempC = (int(tempF) - 32) * 5 / 9
# the output
print('The temperature is ' + str(tempC) + ' Celsius.')
