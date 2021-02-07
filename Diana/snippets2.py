# Snippets Challenge

# Playing with the stock market.

# Write code to take in the name of the client as the user input

name = input("Hi there!\nWhat is your name?:    ")
print("Hello "+ name + "!" )

# Write code to get user input savings" and personalize message with "name"

savings =int(input("What are your current savings?"))
print(f"Wow, thats amazing, you have $ {savings} to invest.")

stock = input("The avaible stocks are Apple, Amazon, Facebook, Google and Microsoft.\nWhich of these would you like to see the breakdown on?" )  
print(f"Great choice {name}! We love {stock}.  ")

Amazon = 3000
Apple = 100
Facebook = 250
Google = 1400
Microsoft = 200

if stock == "Amazon": 
    price = (3000)
    shares = (savings / Amazon)
elif stock == "apple":
    price = (100)
    shares = (savings / Apple) 
elif stock == "facebook":
    price = (250)
    shares = (savings / Facebook)
elif stock == "google":
    price = (1400)
    shares = (savings / Google)
elif stock == "microsoft":
    price = (200)
    shares = (savings / Microsoft)




#else


# Perform user-specific calculation
print(f"Based on the information provided "(name)"  has "{savings}" and can purchase {shares} at $"{price}".")
