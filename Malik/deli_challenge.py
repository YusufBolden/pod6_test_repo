print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for cap in range(len(meats)):
    meats[cap] = meats[cap].capitalize()

for cap in range(len(cheeses)):
    cheeses[cap] = cheeses[cap].capitalize() 

print()

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')

sandwiches.append('Good Burger')

print(sandwiches)

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

order = input('Welcome to Good Burger home of the Good Burger can I take your order?') 
for sandwich in sandwiches:
    if order == sandwich:
        print(f'Great choice! 1 {order} coming right up!')
        break
