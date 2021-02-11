print("Challenge: Favourite Restaurants")
#1


 

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
print()
print(f'The {restaurant["name"]} is located at {restaurant["latitude"]} and {restaurant["longitude"]}')
print()
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(f'The address to {restaurant["name"]} is,\n{restaurant["address1"]}\n{restaurant["city"]}, {restaurant["state"]}.\n{restaurant["zip_code"]}')
print()
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(f'The website for {restaurant["name"]} can be found here:\n{restaurant["url"]}')


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)
print()
fav_restaurant1 = {}

fav_restaurant1["name"] = "La Dolce Vita"
fav_restaurant1["address"] = "4444 Broadway Blvd.\nNew York, NY.\n10051"
fav_restaurant1["favourite_dish"] = "Linguini and clams"

fav_restaurant2 = {}

fav_restaurant2["name"] = "El Tecalote"
fav_restaurant2["address"] = "1234 Mockingbird Lane\nNew York, NY.\n10050"
fav_restaurant2["favourite_dish"] = "Pazole"

fav_restaurant3 = {}

fav_restaurant3["name"] = "Dukes"
fav_restaurant3["address"] = "900 Hi St.\nNew York, NY.\n99999"
fav_restaurant3["favourite_dish"] = "Beer"
print()


 

# TODO: Print each dictionary
print(fav_restaurant1)
print()
print(fav_restaurant2)
print()
print(fav_restaurant3)

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
fav_restaurant3.pop("favourite_dish")
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print(fav_restaurant3)

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
fav_restaurant1["address"] = '3000 Putnam Pl.\nNew York, NY.\n10053'
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(fav_restaurant1["address"])
# TODO: Print the updated dictionary.

print()
print(fav_restaurant1)
