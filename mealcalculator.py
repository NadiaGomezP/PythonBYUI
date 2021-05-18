child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
sales_tax = float(input('What is the sales tax rate? '))

print()

subtotal = (child_meal * children) + (adult_meal * adults)
sales = (subtotal * sales_tax) / 100
total = (subtotal + sales)

print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales:.2f}')
print(f'Total: ${total:.2f}')

payment = float(input('\nWhat is your payment amount? '))
tip = float(input('How much tip do you want to give to the seller? '))


change = (payment - total - tip)

print(f'Change: ${change:.2f}')
print('Thanks for using the Meal Price Calculator!')
