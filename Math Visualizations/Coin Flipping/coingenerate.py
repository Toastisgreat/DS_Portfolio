import numpy as np
import pandas as pd
import time

pvals = np.arange(0,1,0.05) #Check each p value between 0 and 1 within 2 decimal points, currently at 0.05 to see if it works at all
trials = 2000000 # 2 Million trials
winners = {}
start = time.time()


for pnum, p in enumerate(pvals):
    pnum += 1
    if p == 0:
        winners[p] = [0,0]
    else:
        betty = 0
        amy = 0
        print(f'Currently running p={p}\n', end='\r')
        for trial in range(trials):
            #print(f'Running Trial {trial}', end='\r')
            flipstr = ''
            nowin = True
            while nowin: #Simulating each flip
                flip = np.random.rand()
                if p >= flip:
                    flipstr += 'H' #it landed heads
                else:
                    flipstr += 'T' #it landed tails
                if 'HHH' in flipstr: #Betty wins 3 heads
                    nowin = False
                    betty += 1
                elif 'HTH' in flipstr: #Amy wins if HRH
                    amy += 1
                    nowin = False
            flipstr = None
            nowin = None

            if (time.time() -start) / 40 > pnum + 1: # After 40 seconds we break because it's taking tooooo long.
                break

        winners[p] = [betty, amy]


bettywins = np.transpose(np.array([value[0] for value in winners.values()]))
amywins = np.transpose(np.array([value[1] for value in winners.values()]))
pvals = np.transpose(np.array([key for key in winners.keys()]))
fullarray = np.transpose(np.array([pvals, bettywins, amywins]))
frame = pd.DataFrame(data=fullarray)
frame.to_csv('./coinsimulation.csv')
