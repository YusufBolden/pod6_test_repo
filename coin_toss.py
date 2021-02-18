import random
from tqdm import trange, tqdm
from random import randint

numlist = []
for i in range(10):
    numlist.append(random.randint(1, 15))
print(numlist)

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
print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")

# Nested for-loop
num_games = 5

for game in tqdm(range(num_games), desc='Overall Progress'):
    heads = 0
    tails = 0
    
    for j in trange((10000000), desc=f'Game {game+1} Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print(f'Heads: {heads}, Tails: {tails}')
    print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")


