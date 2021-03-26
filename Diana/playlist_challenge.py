#Music playlist challenge!
#In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
#All of your functions should be in the other script (playlist_functions.py)
#But, you'll run your functions here

# 1 Import all the functions in the playlist_functions.py

from playlist_functions import *
import numpy as np 


#This code initializes your playlist as an empty list. no songs in it yet!

my_playlist = []

#2 Check what is in your playlist using the display_plylist() function
# Hint: the display_playlist() function in playlist_functions.py to figure out how to use it
print('Question 2')

# function call
display_playlist(my_playlist)

# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)

'''
example_song ={'artist':'Lauryn Hill','title':'Everything is Everything'}
'''
add_song(my_playlist, {'artist':'Bob Marley','title':'Jammin'})

# 4 Check that you've added the song by running the display_playlist() function again
display_playlist(my_playlist)

add_song(my_playlist, {'artist':'Erykah Badu', 'title':'Didnt ya know?'})
add_song(my_playlist, {'artist':'Kendrick Lamar', 'title':'DNA'})


print('Question 4')

# 5 Add 2 more songs to my_playlist, then display it again using the display_function() function

print('Question 5')
display_playlist(my_playlist)