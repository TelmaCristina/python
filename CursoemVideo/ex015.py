# Write a code that will ask how many km was travelled for rented car went and how many days the car was rented for.
# Check how much the person had to pay, knowing that the rent is $60 per day and $0.15 per km.

days = int(input('How many days did you travelled? '))
km = float(input('How many km did you travelled per day? '))
price = (days * 60) + (km * 0.15)
print('I have travelled for {} days and the amount paid was {:.2f}'.format(days, price))



