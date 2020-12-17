from utils import *
import re
import copy
from functools import *
from collections import *

def main():
    # Load all lines
    lines = getlines()
    cubes = defaultdict(bool)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            active = lines[x][y] == '#'
            cubes[(x, y, 0)] = active
    for _ in range(6):
        cubes_copy = copy.deepcopy(cubes)
        points_to_consider = set()
        for x, y, z in list(cubes_copy):
            if cubes_copy[(x, y, z)]:
                for xn in range(x-1, x+2):
                    for yn in range(y-1, y+2):
                        for zn in range(z-1, z+2):
                            points_to_consider.add((xn, yn, zn))
        for x, y, z in points_to_consider:
            active = cubes_copy[(x, y, z)]
            activect = 0
            neighbors = set()
            for xn in range(x-1, x+2):
                    for yn in range(y-1, y+2):
                        for zn in range(z-1, z+2):
                            neighbors.add((xn, yn, zn))
            neighbors.remove((x, y, z))
            for n in neighbors:
                if cubes_copy[n]:
                    activect += 1
            if active and (activect != 2 and activect != 3):
                cubes[(x, y, z)] = False
            elif not active and activect == 3:
                cubes[(x, y, z)] = True
        nactive = 0
        for v in cubes.values():
            if v:
                nactive += 1
        p(nactive)
        
if __name__ == '__main__':
    main()
