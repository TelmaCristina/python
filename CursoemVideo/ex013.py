# Show new salary with an increase of 15%
salary = float(input('What is your salary? '))
new_salary = salary + (salary * 15 / 100)
print('Your new salary with an increase of 15% is {:.2f}'.format(new_salary))