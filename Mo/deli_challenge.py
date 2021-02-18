
print('Question 1')
print('--------------------------------------------------')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']


#iterator [i] will use .capitalize() to capitalize each item in the list 

for i in range(len(meats)):
    meats[i] = meats[i].capitalize()
    print(meats[i])

for k in range(len(cheeses)):
    cheeses[k] = cheeses[k].capitalize()
    print(cheeses[k])
# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
print('--------------------------------------------------')
print()



print('Question 2')
print('--------------------------------------------------')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list



# a user defined list was created named 'sandwiches'... 
# Once i run a nested loop for meats & cheeses, the combinations of these items need to added to this list.
#  this is the sandwich section our our menu which users will order from.... 


sandwiches = []
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')
print(sandwiches)
print('--------------------------------------------------')
print()


print('Question 3')
print('--------------------------------------------------')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'


#Question 3 is smilar to the restarant challenge
# i need to create a user input variable named 'order' asking the customer what they will have 
# i will need to define an iterator to pass through the sandwiches list and check if such combination is available. 
#output statement will entail an 'if' statement with the fstring syntax. 
customer_order = input('What will you have today?')

for sandwich in sandwiches:
    if customer_order == sandwich:
        print(f'Okay? 6 orders of {customer_order}...what is your choice of bread?')
        break 
print('--------------------------------------------------')
print()