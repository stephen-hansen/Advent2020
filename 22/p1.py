from utils import *
import re
import copy
from functools import *
from collections import *
import math

def main():
    # Load all lines
    lines = getlines()
    decks = {}
    pid = 1
    for l in lines:
        if l.startswith('Player'):
            decks[pid] = []
        elif l == '':
            pid += 1
        else:
            decks[pid].append(int(l))

    winner = None
    while True:
        top_1 = decks[1].pop(0)
        top_2 = decks[2].pop(0)
        if top_1 > top_2:
            decks[1].append(top_1)
            decks[1].append(top_2)
        else:
            decks[2].append(top_2)
            decks[2].append(top_1)
        if len(decks[1]) == 0:
            # p2 wins
            winner = 2
            break
        elif len(decks[2]) == 0:
            # p1 wins
            winner = 1
            break
    mult = 1
    score = 0
    while len(decks[winner]) != 0:
        score += mult * decks[winner].pop(len(decks[winner])-1)
        mult += 1
    p(score)
    
if __name__ == '__main__':
    main()
