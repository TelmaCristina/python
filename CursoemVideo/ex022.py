# Write a code that will read the full name of someone and show:
# 1. Name with all letters in uppercase
# 2. Nem with all letters in lowercase
# 3. How many letters in total (without considering the spaces)
# 4. How many letters in the first name

name = str(input('Write your full name: '))
divided = name.split()
print('Your name in upper case is: {}'.format(name.upper()))
print('Your name in lower case is: {}'.format(name.lower()))
print('Your name has {} letters'.format(len(name.strip()) - name.count(' ')))
# print(divided)
print('Your first name is {} and it has {} letters'.format(divided[0], len(divided[0])))
