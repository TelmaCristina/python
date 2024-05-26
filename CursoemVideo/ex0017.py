# Write a code to read the length of the opposite (vertical, a) and adjacent (horizontal, b) cathetus of a triangle.
# Calculate the length of the hypotenuse (line that links both opposite and adjacent cathetus, c)
# Hypotenuse = sqrt(base**2 + height**2) => c = sqrt(a**2 + b**2)

'''
# We can calculate the hypotenuse only using the math concept
import math
co = float(input('Write the length of the opposite cathetus: '))
ca = float(input('Write the length og the adjacent cathetus: '))
hypo = math.sqrt(co ** 2 + ca ** 2) #(co ** 2 + ca ** 2) ** 0.5
print('The hypotenuse of the triangle is {:.2f}'.format(hypo))
'''

'''
import math
a = float(input('Write the length of opposite cathetus: '))
b = float(input('Write the length of the adjacent cathetus'))
c = math.hypot(a, b)
print('The hypotenuse of the triangle is: {:.2f}'.format(c))
'''

# We can import only the method
from math import hypot
a = float(input('Write the length of the opposite cathetus: '))
b = float(input('White the length of the adjacent cathetus: '))
c = hypot(a, b)
print('The hypotenuse of the triangle is: {:.2f}'.format(c))

