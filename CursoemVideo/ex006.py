# Print the double, triple, root and power of a number
n = int(input('Choose a number: '))
d = n * 2
t = n * 3
sq = n ** (1/2)
e = n ** 2
# print('The double of {} is {}'.format(n, d))
# print('The triple of {} is {}'.format(n, t))
# print('The square root of {} is {:.3f}'.format(n, sq))
# print('The power of {} is {}'.format(n, e))

# If no variables are needed, we can print it without variables
print('The double of {} is {}'.format(n, (n * 2)))
print('The triple of {} is {}'.format(n, (n * 3)))
print('The square root of {} is {:.3f}'.format(n, (n ** (1/2))))
print('The power of {} is {}'.format(n, (n ** 2)))
