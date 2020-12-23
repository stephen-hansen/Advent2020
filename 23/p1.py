from utils import *
import re
import copy
from functools import *
from collections import *
import math

def main():
    # Load all lines
    inp = '487912365'
    #inp = '389125467'
    cups = list(inp)
    curr = 0
    currlabel = cups[0]
    for _ in range(100):
        cuplen = len(cups)
        print(f'curr = {currlabel}')
        chosen = [cups[(curr+1)%cuplen], cups[(curr+2)%cuplen], cups[(curr+3)%cuplen]]
        print(f'pick up = {chosen}')
        for cup in chosen:
            cups.remove(cup)
        nextlabel = str(int(currlabel) - 1)
        if nextlabel == '0':
            nextlabel = str(len(inp))
        while nextlabel in chosen:
            nextlabel = str(int(nextlabel) - 1)
            if nextlabel == '0':
                nextlabel = str(len(inp))
        print(f'destination = {nextlabel}')
        nextindex = (cups.index(nextlabel)+1)%len(cups)
        for i in range(len(chosen)):
            to_insert = chosen[len(chosen)-1-i]
            cups.insert(nextindex, to_insert)
        curr = (cups.index(currlabel)+1)%len(cups)
        currlabel = cups[curr]
    print(''.join(cups))

if __name__ == '__main__':
    main()
