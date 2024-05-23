# Give the new price of a product wit 5% of discount
price = float(input('What is the price of the product? '))
new_price = price - (price * 5 / 100)
print('The price with discount is: {:.2f}'.format(new_price))
