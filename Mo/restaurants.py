#Mohgli-Restaurant Challenge

print("Challenge: Favourite Restaurants")
print()
print()
#Dictionary for Four Barrel Coffee
restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}
print()


print("Question 1")
print('----------------------------------------------------------------------------')
# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print("* This is where you can find Four Barrel Coffee. *")
print()
print(f'Latitude: {restaurant["latitude"]}\nLongitude: {restaurant["longitude"]}')
print(f'Address of Four Barrel Coffee: {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["country"]} {restaurant["zip_code"]}')
print(f'Website of Four Barrel Coffee: {restaurant["url"]}')

print('----------------------------------------------------------------------------')


print()
print()


print("Question 2")
print('----------------------------------------------------------------------------')
# TODO: Create a new empty dictionary called fav_restaurants.
# TODO: Choose 3 of your most favourite restaurants in NYC and add the following information for those restaurants inside fav_restaurants:
#         1. Name of the restaurant - Should be the key of the dictionary
#         2. Address of the restaurant - 1st value of the list
#         3. Favourite dish in that restaurant - 2nd value of the list
#         4. Opening and closing hours of that restaurant - 3rd value of the list
# TODO: Print the dictionary.


top3 = {}
top3["Chola"] = ["E 58th St, New York, NY 1002", "Biryani", "5-10 PM"]
top3["Louis & Earnie's Pizza"] = ["1300 Crosby Ave, The Bronx, NY 10461", "Godfather Pie", "11-9 PM"]
top3["Insa"] = ["328 Douglass St, Brooklyn, NY 11217", "Galbi", "3-9 PM"]

print("* These are my favorite Restarurants in New York *")
print()
print(top3)
print('----------------------------------------------------------------------------')

print()
print()
print()



print("Question 3")
print('----------------------------------------------------------------------------')

#print("(Imagine that any 1 of your most favourite restaurants closed down during the Covid. Remove the details of that restaurant from the dictionary fav_restaurants.)")
# TODO: Remove 1 restaurant from the dictionary fav_restaurants.

top3.pop("Chola")


# TODO: Print the new dictionary. The new dictionary should contain only 2 restaurants.

print("Chola closed down at the moment  (true story) :( ... Below are the restaurants currently open for business.")
print(top3)
print('----------------------------------------------------------------------------')
print()
print()



#print("Imagine that another one of your most favourite restaurants modified its opening and closing hours during Covid. Update just the hours field (3rd value of the list) for 1 restaurant in the dictionary fav_restaurants.")
# TODO: Update the hours field of 1 restaurant in the dictionary fav_restaurants.
# TODO: Print the old and new open hours of the restaurant by accessing those fields from the dictionary.
# TODO: Print the updated dictionary.


print("Question 4")
print('----------------------------------------------------------------------------')
print()
old_hours = top3["Louis & Earnie's Pizza"][2]
top3["Louis & Earnie's Pizza"][2] = "5-9pm"
new_hours = top3["Louis & Earnie's Pizza"][2]

print(f"The old hours of Louis & Earnie's Pizza were {old_hours}. The new hours of operation are {new_hours}.")
print()
print()
print('----------------------------------------------------------------------------')



