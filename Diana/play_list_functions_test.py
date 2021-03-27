import pytest
# this makes sure we look at the parent directory to import from the playlist.py file

import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from play_list_functions import *

@pytest.fixture
def playlist():
    return [
            {'artist':'J.Cole', 'title': 'A tale of two cities'},
            {'artist':'Nina Simone', 'title': 'Baltimore'},
            {'artist':'Bridge City Sinners', 'title': 'Ashes'},
            {'artist':'The Dead South', 'title': 'That Bastard Son'},
            {'artist':'Greensky Bluegrass','title': 'Old Barns'},
            {'artist':'Buika','title':'No habra nadie en el mundo'},
            {'artist':'A$AP Ferg','title':'New Level'},
            {'artist':'J.COLE', 'title':'ATM'}
    ]


# Question 1:Complete the test for get_playlist_titles () function

def test_get_titles(playlist):
    assert get_playlist_titles(playlist) ==['A tale of two cities','Baltimore','Ashes','That Bastard Son','Old Barns','no habra nadie en el mundo','New Level']

# Question 2: Write two test functions for search_by_artist

def test_artist_search(playlist):
    assert search_by_artist(playlist, 'J.COLE') == ['A tale of two cities','ATM']

def test_artist_search(playlist):
    assert search_by_artist(playlist, 'The Dead South') ==['That Bastard Son']

# Question 3: Write two test functions for search_by_title

def test_search_by_title(playlist):
    assert search_by_title(playlist, 'New Level') == [
                                                        {'artist': 'A$AP Ferg'}
                                                        ]

def test_search_by_title(playlist):
    assert search_by_title(playlist, 'Buika') == [
                                                        {'artist': 'Buika'}
                                                        ]


print(get_playlist_titles(playlist))