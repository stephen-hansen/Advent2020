from utils import *
import re
import copy
from functools import *
from collections import *
import math

def main():
    # Load all lines
    lines = getlines()
    tiles = {}
    tid = None
    for l in lines:
        if l.startswith('Tile'):
            pat = re.compile(r'Tile (\d+):')
            tid = int(re.fullmatch(pat, l).group(1))
            tiles[tid] = []
        elif l == '':
            continue
        else:
            tiles[tid].append(l)

    borders = {}
    for tid, lines in tiles.items():
        length = len(lines)
        length2 = len(lines[0])
        east = ''
        west = ''
        for l in lines:
            east += l[length2-1]
            west += l[0]
        bs = [lines[0], east, lines[length-1], west]
        borders[tid] = bs

    numtiles = len(borders)
    dim = int(math.sqrt(numtiles))
    
    grid = []
    for i in range(dim):
        grid.append([])
        for _ in range(dim):
            grid[i].append(None)

    corners = []
    for tid, bords in borders.items():
        nmatch = 0
        for tid2, bords2 in borders.items():
            if tid == tid2:
                continue
            for b in bords:
                for b2 in bords2:
                    if b == b2 or b == b2[::-1]:
                        nmatch += 1
        p(nmatch)
        if nmatch == 2:
            corners.append(tid)

    r = 1
    for c in corners:
        r *= c
    p(r)

    
if __name__ == '__main__':
    main()
