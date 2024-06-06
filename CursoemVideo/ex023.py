# Write a code to read a number from 0 to 9999
# Show on the screen each one of the digits by itself
# Ex:. 1834 - Unity: 4, ten: 3, hundred: 8, thousand: 1
'''
# In this way, we only can use numbers with 4 digits
num = int(input('Write a number: '))
n = str(num)
print('Unity {}'.format(n[3]))
print('Ten {}'.format(n[2]))
print('Hundred {}'.format(n[1]))
print('Thousand {}'.format(n[0]))
'''

# In this case we can choose any number from 0 to 9999
num = int(input('Write a number: '))
u = num // 1 % 10
d = num // 10 % 10
h = num // 100 % 10
t = num // 1000 % 10
print('Analysing the number {}'.format(num))
print('Unity: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundreds: {}'.format(h))
print('Thousands: {}'.format(t))


