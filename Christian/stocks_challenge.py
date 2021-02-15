#print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

#print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_name = input("Hi, please type your name here in order to get to know you better?: ")
# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = int(input(f"Tell me {client_name}, how much do you have in your savings?: "))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
client_stock = input("Which stock would you be interested in purchasing? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.: ")

#print(client_name)
#print(savings_total)
#print (stock)

#print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if client_stock == "amzn":
    stock_price = amazon
    num_stocks = client_savings/stock_price
elif client_stock == "aapl":
    stock_price = apple
    num_stocks = client_savings/stock_price
elif client_stock == "fb":
    stock_price = fb
    num_stocks = client_savings/stock_price
elif client_stock == "goog":
    stock_price = google
    num_stocks = client_savings/stock_price
elif client_stock == "msft":
    stock_price = msft
    num_stocks = client_savings/stock_price
else:
    stock_price = "n/a"   
    


'''amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

if stock_price == "n/a":
    print("Not the right in put")
else:
    print(f"{client_name} has {client_savings} in savings and you can buy {num_stocks} shares of {client_stock} at the current price of ${stock_price} per share")     




#print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()

