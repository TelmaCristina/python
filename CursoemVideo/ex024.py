# Write a code to read the name of a city
# Find out if the city starts with word 'New'

city = str(input('Choose a city: ')).strip()
print(city[:3].lower() == 'new')