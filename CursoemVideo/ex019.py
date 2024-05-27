# The teacher wants to randomly take a student to help him to clean the blackboard.
# Write a code that will read the name of the students, and will randomly choose one.
import random

# Creating a list
name = ['Telma', 'Cris', 'Pri', 'Betia', 'Paula', 'Veronica', 'Elsi', 'Kellen']
select_name = random.choice(name)
print('The selected student is: {}'.format(select_name))


# Now let's choose only among 4 students
student1 = str(input('The first student is: '))
student2 = str(input('The second student is: '))
student3 = str(input('The third student is: '))
student4 = str(input('The fourth student is: '))
students_list = [student1, student2, student3, student4]
the_chosen = random.choice(students_list)
print('The chosen student is: {}'.format(the_chosen))



