# Print the distance in meter and its correspondent number in cm, mm and km
n = float(input('The distance in meter: '))
c = n * 100
mm = n * 1000
km = n * 0.001
print(n, ' meters is equal to: {:.0f}cm, {:.0f}mm and {}km'.format(c, mm, km))



