# Print a number with the number before and after it
n = int(input('Choose a number: '))
n_before = n - 1
n_after = n + 1
print('The number before {} is {}'.format(n, n_before))
print('The number after {} is {}'.format(n, n_after))

# If I only want to display the result, no need of variable
# print('The number before and after {} is {} and {}'.format(n, (n-1), (n+1)))
