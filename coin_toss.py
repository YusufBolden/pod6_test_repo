from random import randint
from tqdm.notebook import tdqm, trange

heads = 0
tails = 0

for flip in tqdm(range(1000000)), desc='Coin Flip Progress':
    toss = randint(0, 1)
    if toss == 0:
        heads += 1
    else:
        tails += 1