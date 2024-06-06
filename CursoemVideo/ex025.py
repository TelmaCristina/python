# Write a code to read a full name
# Find out if the person has the surname 'Silva'

name = str(input('Write your full name: ')).strip()
print('Do you have Silva in your name? {}'.format('silva' in name.lower()))
