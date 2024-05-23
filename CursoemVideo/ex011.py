# Write a code that reads the wall height and wall width in meters
# Check its area and the amount of paint needed to paint the wall
# Each litre of paint is enough for 2m**2

wh = float(input('What is the wall height? '))
ww = float(input('What is the wall width? '))
area = wh * ww
# For each 2m we need 1 litre of paint
paint = area / 2
print('The wall dimension is {} x {} and its area is {}m2'.format(wh, ww, area))
print('To paint the wall you will need {} litres of paint'.format(paint))