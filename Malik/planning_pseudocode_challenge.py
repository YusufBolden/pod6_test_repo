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
order1 = {'destination':'Brooklyn', 'date_shipped': '01/10/21', 'weight': 50.5}
order2 = {'destination':'Baltimore', 'date_shipped': '01/15/21', 'weight': 5}
order3 = {'destination':'Atlanta', 'date_shipped': '02/03/21', 'weight': 120.5}


'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 
Print out the database to make sure all the info is in there. 
'''
print('\nPART 2')
order_database_list = [order1, order2, order3]
print(order_database_list)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

order4 = {'destination':'Austin', 'date_shipped': '2/18/21', 'weight': 5.8}
order5 = {'destination':'Miami', 'date_shipped': '3/01/21', 'weight': 10}

def add_order_list(database, order):
	database.append(order)

add_order_list(order_database_list, order4)
add_order_list(order_database_list, order5)
print(order_database_list)

print(order_database_list)
'''
4. Define a function called complete_order() to mark a specific order in your database complete
This means you'll need a new piece of data inside the order that is True when the order is complete.
Test this out and print out your database to make sure it works!
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')
def complete_order_list(database, order_index):
    database[order_index]['complete'] = True

complete_order_list(order_database_list, 1)
complete_order_list(order_database_list, 3)
print(order_database_list)
