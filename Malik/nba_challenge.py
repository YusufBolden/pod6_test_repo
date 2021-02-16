print("Challenge 2.1:")

# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
# TODO: Create variable here for number of 3 pt shots made by James Harden

jamal_3pts_made = 43
fred_3pts_made = 86
james_3pts_made = 57

print("Challenge 2.2:")

print(str"In the 2021 NBA season, Jamal Murray has made {jamal_3pts_made} 3 point shots")

# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden

print(str"In the 2021 NBA season, Fred VanVleet has made {fred_3pts_made} 3 point shots")
print(str"In the 2021 NBA season, James Harden has made {james_3pts_made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
# TODO: Create variable here for number of 3 pt shot attempts by James Harden

jamal_3pts_attempted = 126
fred_3pts_attempted = 216
james_3pts_attempted = 161 

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."

print(f"This NBA season, Jamal Murray has made {jamal_3pts_made} " f"3 point shots and attempted {jamal_3pts_attempted} 3 point shots")
print(f"This NBA season, Fred VanVleet has made {fred_3pts_made} " f"3 point shots and attempted {fred_3pts_attempted} 3 point shots")
print(f"This NBA season, James Harden has made {james_3pts_made} " f"3 point shots and attempted {james_3pts_attempted} 3 point shots")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
# TODO: Calculate and print the 3 point percentage for James Harden

jamal_m_3pts_percentage = jamal_3pts_made/jamal_3pts_attempted
fred_v_3pts_percentage = fred_3pts_made/fred_3pts_attempted
james_h_3pts_percentage = james_3pts_made/james_3pts_attempted
print(f"This season Jamal Murry's 3 point percentage is {jamal_m_3pts_percentage}")
print(f"This season Fred VanVleet's 3 point percentage is {fred_v_3pts_percentage}")
print(F"This season James Harden's 3 point percentage is {james_h_3pts_percentage}")


print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers

lakers_are_the_best = True
print(f'The statement that the Lakers are the best NBA team is \ {lakers_are_the_best}.')

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
# TODO: Convert your `lakers_are best` variable to a float, and print it out

print(int(lakers_are_the_best))
print(float(lakers_are_the_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

print(str(jamal_m_3pts_percentage))
print(str(fred_v_3pts_percentage))
print(str(james_h_3pts_percentage))

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(jamal_m_3pts_percentage))
print(int(fred_v_3pts_percentage))
print(int(james_h_3pts_percentage))