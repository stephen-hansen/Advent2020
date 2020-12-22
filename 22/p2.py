from utils import *
import re
import copy
from functools import *
from itertools import *
from collections import *
import math

def to_hash(decks):
    return '1:' + ','.join([str(x) for x in decks[1]]) + ';2:' + ','.join([str(y) for y in decks[2]])

def game(decks):
    ROUNDS = set()
    winner = None
    while True:
        top_1 = decks[1].popleft()
        top_2 = decks[2].popleft()
        hashed = (tuple(decks[1]), tuple(decks[2]))
        rwinner = None
        if hashed in ROUNDS:
            return 1
        ROUNDS.add(hashed)
        if len(decks[1]) >= top_1 and len(decks[2]) >= top_2:
            next_decks = {}
            next_decks[1] = deque(list(islice(decks[1], 0, top_1)))
            next_decks[2] = deque(list(islice(decks[2], 0, top_2)))
            rwinner = game(next_decks)
        elif top_1 > top_2:
            rwinner = 1
        else:
            rwinner = 2
        if rwinner == 1:
            decks[1].append(top_1)
            decks[1].append(top_2)
        elif rwinner == 2:
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
    return winner


def main():
    # Load all lines
    lines = getlines()
    decks = {}
    pid = 1
    for l in lines:
        if l.startswith('Player'):
            decks[pid] = deque([])
        elif l == '':
            pid += 1
        else:
            decks[pid].append(int(l))

    winner = game(decks)
    mult = 1
    score = 0
    while len(decks[winner]) != 0:
        score += mult * decks[winner].pop()
        mult += 1
    p(score)
    
if __name__ == '__main__':
    main()
