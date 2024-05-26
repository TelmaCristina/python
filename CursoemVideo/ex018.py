# Write a code to read the value of sine, cosine and tangent of an angle
# sine = opposite cathetus / hypotenuse
# cosine = adjacent cathetus / hypotenuse
# tan = opposite cathetus / adjacent cathetus

'''
import math
angle = float(input('Write the value of the angle: '))
# we need to change it to radians
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print('The sine of {} is {:.2f}'.format(angle, sine))
print('The sine of {} is {:.2f}'.format(angle, cosine))
print('The sine of {} is {:.2f}'.format(angle, tangent))
'''

from math import radians, sin, cos, tan
angle = float(input('Write the value of the angle: '))
# we need to change it to radians
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('The sine of {} is {:.2f}'.format(angle, sine))
print('The sine of {} is {:.2f}'.format(angle, cosine))
print('The sine of {} is {:.2f}'.format(angle, tangent))
