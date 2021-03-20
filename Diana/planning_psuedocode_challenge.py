'''
Planning & pseudocode challenge!
For each piece here, write out the pseudocode as comments FIRST, then write your code!
At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping
You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)
Will you choose to make each shipping order as a dictionary or list? Why?
Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')
'''

'''
order_1 = {'destination':'Washington'},{'date_shipped':'03/11/2020'},{'weight':75.00}

order_2 = {'destination':'Chicago'},{'date_shipped':'03/11/2020'},{'weight':120.00}

order_3 = {'destination':'Austin'},{'date_shipped':'03/11/2021'},{'weight':43.00}



'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')

orders =[order_1,order_2,order_3]

print(orders)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

def add_order(database,order):
  orders.append(order)

add_order(orders,order_4)
add_order(orders,order_5)

print(orders)
'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')
