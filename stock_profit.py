#!/usr/bin/python3
from collections import Counter
import time
import itertools
import numpy as np

def stockPairs(stocksProfit, target):
    """Solution 1 """
    a = set()
    n = len(stocksProfit)
    for indice,v in enumerate(stocksProfit):
        for i in stocksProfit[indice+1:n]:
            if v + i ==target:
                a.add((i,v) if v > i else (v,i))
    return len(a)


def stockPairs(stocksProfit, target):
    """Solution 1 """
    s = set()
    all_combinations = itertools.combinations(stocksProfit, 2)
    for combination in all_combinations:
        if sum(combination) == target:
            s.add(tuple(sorted(combination)))
    return len(s)

def stockPairs(s,t):
    mesh = np.array(np.meshgrid(s))
    combinations = mesh.T.reshape(2)

    print(combinations)

############
with open('in.txt') as f:
    lines = f.read().splitlines()
    
s =  [5, 7, 9, 13, 11, 6, 6, 3, 3]

t = 12
start_time = time.time()
print(stockPairs(s,t))
print("--- %s seconds ---" % (time.time() - start_time))
