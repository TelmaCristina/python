from math import trunc
# trunc () method returns the truncated integer part of a number.

# Write a code to read a real number from input and its whole portion
num = float(input('Choose a number: '))
print('The whole portion of {} is {}'.format(num, trunc(num)))

# There is also a way to do this exercise without importing the library
num2 = float(input('Choose a number: '))
print('The whole number of {} is {}'.format(num2, int(num2)))