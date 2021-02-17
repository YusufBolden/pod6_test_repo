from tqdm import trange, tqdm
from random import randint

'''
note: If you receive an ImportError, NameError or message stating there is no module named tqdm, run the following in your terminal:
    python -m pip install tqdm
you may also have to run:
    python -c 'import tqdm'
'''

# for-loop

heads = 0
tails = 0

for i in tqdm(range(10000000), desc='Coin Flip Progress'):
    toss = randint(0, 1)
    if toss == 0:
        heads += 1
    else:
        tails += 1
print(heads, tails)

# Nested for-loop
num_games = 3

for game in trange(num_games, desc='Overall Progress'):
    heads = 0
    tails = 0
    
    for j in trange((10000000), desc=f'Game {game+1} Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print(f'Heads: {heads}, Tails: {tails}')

