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

    for _ in range(100):
        tiles_to_look_at = set()
        for pos, color in hexagrid.items():
            if color:
                # Black tile
                tiles_to_look_at.add(pos)
                # Add neighbors
                near = [[1, 0], [-1, 0], [0.5, -1], [-0.5, 1], [0.5, 1], [-0.5, -1]]
                plist = list(pos)
                neighbors = []
                for n in near:
                    neighbors.append((plist[0] + n[0], plist[1] + n[1]))
                for n in neighbors:
                    tiles_to_look_at.add(n)
        
        next_grid = copy.deepcopy(hexagrid)
        for t in tiles_to_look_at:
            color = hexagrid[t]
            near = [[1, 0], [-1, 0], [0.5, -1], [-0.5, 1], [0.5, 1], [-0.5, -1]]
            plist = list(t)
            neighbors = []
            for n in near:
                neighbors.append(hexagrid[(plist[0] + n[0], plist[1] + n[1])])
            num_black_tiles = sum(neighbors)

            if color:
                if num_black_tiles == 0 or num_black_tiles > 2:
                    next_grid[t] = False
            else:
                if num_black_tiles == 2:
                    next_grid[t] = True
        
        hexagrid = next_grid
    
        nblack = 0
        for pos, color in hexagrid.items():
            if color:
                nblack += 1
        p(nblack)
    
if __name__ == '__main__':
    main()
