
print("Challenge: Favourite Restaurants")

print()
print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 
Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


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



# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.


print(restaurant['latitude']), print(restaurant['longitude'])
print(f'Four Barrel Coffee address is {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["country"]} {restaurant["zip_code"]}')
print(restaurant['url'])

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)


# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

favrestaurant_1  = {    "name": "Burger King",    "address" : "1935 Coney Island Ave, Brooklyn, NY 11230", "fav_dish" : "Whopper"    }                                                                                                                                                                                     
favrestaurant_2  = {    "name": "Micheal's",    "address" : "2929 Avenue R, Brooklyn, NY 11229",    "fav_dish" : "Baked Clams"    }
favrestaurant_3  = {    "name": "The Juicy Box",    "address" : "2281 Nostrand Ave., Brooklyn, NY 11210",   "fav_dish" : "Salmon Burger"}

print(favrestaurant_1)
print(favrestaurant_2)
print(favrestaurant_3)

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

favrestaurant_2.pop('fav_dish')
print(favrestaurant_2)

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

favrestaurant_3.update({'address': '1715 Flatbush Ave, Brooklyn, NY 11210'})
print(favrestaurant_3)