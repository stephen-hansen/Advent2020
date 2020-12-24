from utils import *
import re
import copy
from functools import *
from collections import *
import math

def main():
    # Load all lines
    lines = getlines()
    pattern = re.compile(r'(e|se|sw|w|nw|ne)')
    hexagrid = defaultdict(bool) # False = white, True = black
    start = [0.0, 0.0] # x, y
    # e/w, se/nw, ne/sw
    for l in lines:
        pos = copy.deepcopy(start)
        for m in re.finditer(pattern, l):
            direction = m.group(1)
            if direction == 'e':
                pos[0] += 1
            elif direction == 'w':
                pos[0] -= 1
            elif direction == 'se':
                pos[0] += 0.5
                pos[1] -= 1
            elif direction == 'nw':
                pos[0] -= 0.5
                pos[1] += 1
            elif direction == 'ne':
                pos[0] += 0.5
                pos[1] += 1
            elif direction == 'sw':
                pos[0] -= 0.5
                pos[1] -= 1
        hexagrid[tuple(pos)] = (not hexagrid[tuple(pos)])

    nblack = 0
    for pos, color in hexagrid.items():
        if color:
            nblack += 1
    p(nblack)

    
if __name__ == '__main__':
    main()
