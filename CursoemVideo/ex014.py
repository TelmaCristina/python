# Check temperature in Fahrenheit and Celsius

# Fahrenheit to Celsius
f = float(input('Input a temperature in Fahrenheit '))
celsius = (f - 32) / 1.8
print('The temperature of {:.1f} Fahrenheit is {:.1f} in Celsius'.format(f, celsius))

# celsius to Fahrenheit
c = float(input('Input a temperature in Celsius '))
fahrenheit = ((9 * c) / 5) + 32
print('The temperature of {:.1f} in Celsius is {:.1f} in Fahrenheit'.format(c, fahrenheit))

