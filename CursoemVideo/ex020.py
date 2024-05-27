# A teacher wants to choose in which order the student will present their homework
# Write a program which will read the name of 4 students and the order they were randomly picked.
from random import shuffle
student1 = str(input('First student: '))
student2 = str(input('Second student: '))
student3 = str(input('Third Student: '))
student4 = str(input('Fourth student: '))
students = [student1, student2, student3, student4]
# Use the method shuffle to put the list in a random order every time you run the code.
shuffle(students)
print('The order of students is: ')
print(students)
