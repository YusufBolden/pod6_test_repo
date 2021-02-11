print("Challenge 2.1:")
jamal_murray_3pts_made = 46
james_harden_3pts_made = 37
fred_vanfleet_3pts_made = 43


print(jamal_murray_3pts_made)
print(fred_vanfleet_3pts_made)
print(james_harden_3pts_made)

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playodds, Fred VanVleet {fred_vanfleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden {james_harden_3pts_made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109

print(jamal_murray_3pts_attempts)
print(fred_vanvleet_3pts_attempts)
print(james_harden_3pts_attempts)


print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} and attempted {jamal_murray_3pts_attempts} 3 point shots.")
print(f"In the 2020 NBA Playoffs Fred Vanvleet made {fred_vanfleet_3pts_made} and attempted {fred_vanvleet_3pts_attempts} 3 point shots.")
print(f"In the 2020 NBA Playoffs James Harden made {james_harden_3pts_made} and attempted {james_harden_3pts_attempts} 3 point shots.")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
jamal_murray_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
fred_vanvleet_percentage = fred_vanfleet_3pts_made/fred_vanvleet_3pts_attempts
james_harden_percentage = james_harden_3pts_made/james_harden_3pts_attempts
print(jamal_murray_percentage)
print(fred_vanvleet_percentage)
print(james_harden_percentage)

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
paragraph="The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(paragraph.upper())

# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')

lakers_are_best = False
print(f'The statement that the Lakers are the best NBA team is \
{lakers_are_best}.')


print('Challenge 3.4: Type Conversion')

print(int(lakers_are_best))
print(float(lakers_are_best))

print(str(jamal_murray_percentage))
print(str(fred_vanvleet_percentage))
print(str(james_harden_percentage))

#convert to integer
print(int(jamal_murray_percentage))
print(int(fred_vanvleet_percentage))
print(int(james_harden_percentage)) 