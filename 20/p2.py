from utils import *
import re
import copy
from functools import *
from collections import *
import math

class Tile:
    def __init__(self, lines, tid):
        self.lines = lines
        self.connects = [None, None, None, None] # Up, Left, Down, Right
        self.tid = tid

    def rotate_left(self, rotated=set()):
        self.lines = rotate_left(self.lines)
        self.connects = [self.connects[3], self.connects[0], self.connects[1], self.connects[2]]
        rotated.add(self.tid)
        for c in self.connects:
            if c is not None and c.tid not in rotated:
                rotated = rotated.union(c.rotate_left(rotated))
        return rotated

    def mirror_vertical(self, mirrored=set()):
        self.lines = mirror_vertical(self.lines)
        self.connects = [self.connects[0], self.connects[3], self.connects[2], self.connects[1]]
        mirrored.add(self.tid)
        for c in self.connects:
            if c is not None and c.tid not in mirrored:
                mirrored = mirrored.union(c.mirror_vertical(mirrored))
        return mirrored

    def mirror_horizontal(self, mirrored=set()):
        self.lines = mirror_horizontal(self.lines)
        self.connects = [self.connects[2], self.connects[1], self.connects[0], self.connects[3]]
        mirrored.add(self.tid)
        for c in self.connects:
            if c is not None and c.tid not in mirrored:
                mirrored = mirrored.union(c.mirror_horizontal(mirrored))
        return mirrored

    def get_borders(self):
        north = self.lines[0]
        south = self.lines[len(self.lines)-1][::-1]
        east = ''
        west = ''
        for l in self.lines:
            east = east + l[len(l)-1]
            west = l[0] + west
        return [north, west, south, east]

def merge_tiles(tile):
    row = 0
    col = 0
    row_jmp = len(tile.lines)-2
    col_jmp = len(tile.lines[0])-2
    merged = []
    n_rows = 0
    temp = tile
    while temp != None:
        n_rows += 1
        temp = temp.connects[2]
    for i in range(n_rows):
        for j in range(row_jmp):
            merged.append('')
    while tile != None:
        tile2 = tile
        while tile2 != None:
            for i in range(1, row_jmp+1):
                merged[(i-1)+row_jmp*row] += tile2.lines[i][1:-1]
            tile2 = tile2.connects[3]
            col += 1
        tile = tile.connects[2]
        row += 1
        col = 0
    p('\n'.join(merged))
    p(len(merged))
    p(len(merged[0]))
    return merged

def merge_tiles_debug(tile):
    row = 0
    col = 0
    row_jmp = len(tile.lines)
    col_jmp = len(tile.lines[0])
    merged = []
    n_rows = 0
    temp = tile
    while temp != None:
        n_rows += 1
        temp = temp.connects[2]
    for i in range(n_rows):
        for j in range(row_jmp):
            merged.append('')
    while tile != None:
        tile2 = tile
        while tile2 != None:
            for i in range(0, row_jmp):
                merged[i+row_jmp*row] += tile2.lines[i]
            tile2 = tile2.connects[3]
            col += 1
        tile = tile.connects[2]
        row += 1
        col = 0
    p('\n'.join(merged))
    p(len(merged))
    p(len(merged[0]))
    return merged

def find_pattern(lines):
    pattern = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
    total = 0
    for _ in range(4):
        for _ in range(2):
            total += find_pattern_implicit(lines, pattern)
            lines = mirror_vertical(lines)
        lines = rotate_left(lines)
    return total

def find_pattern_implicit(lines, pattern):
    lines = [list(l) for l in lines]
    pattern_y = len(pattern)
    pattern_x = len(pattern[0])
    total = 0
    nseamonsters = 0
    for starti in range(0, len(lines)-pattern_y):
        for startj in range(0, len(lines[0])-pattern_x):
            all_match = True
            for i in range(starti, starti+pattern_y):
                if not all_match:
                    break
                for j in range(startj, startj+pattern_x):
                    c = pattern[i-starti][j-startj]
                    compare = lines[i][j]
                    if c == '#' and compare != '#':
                        all_match = False
                        break
            if all_match:
                # Found a monster
                nseamonsters += 1
                for i in range(starti, starti+pattern_y):
                    for j in range(startj, startj+pattern_x):
                        c = pattern[i-starti][j-startj]
                        compare = lines[i][j]
                        if c == '#' and compare == '#':
                            lines[i][j] = 'O'
    debug_lines = '\n'.join([''.join(l) for l in lines])
    p(debug_lines)
    for l in lines:
        for c in l:
            total += (c == '#')
    if nseamonsters > 0: 
        return total
    else:
        return 0

def rotate_left(lines):
    new_lines = []
    for l in lines:
        new_lines.append('')
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            new_lines[len(lines)-1-j] += lines[i][j]
    return new_lines

def mirror_vertical(lines):
    new_lines = []
    for l in lines:
        new_lines.append(l[::-1])
    return new_lines

def mirror_horizontal(lines):
    new_lines = []
    for l in lines:
        new_lines.insert(0, l)
    return new_lines

def main():
    # Load all lines
    lines = getlines()
    old_tiles = {}
    tiles = {}
    tid = None
    for l in lines:
        if l.startswith('Tile'):
            pat = re.compile(r'Tile (\d+):')
            tid = int(re.fullmatch(pat, l).group(1))
            old_tiles[tid] = []
        elif l == '':
            continue
        else:
            old_tiles[tid].append(l)
    
    for tid, lines in old_tiles.items():
        tiles[tid] = Tile(lines, tid)

    matched = set()

    for tid, tile in tiles.items():
        for tid2, tile2 in tiles.items():
            if tile.tid == tile2.tid:
                continue
            borders = tile.get_borders()
            borders2 = tile2.get_borders()
            skip = False
            for i in range(len(borders)):
                if skip:
                    break
                for j in range(len(borders2)):
                    bord1 = borders[i]
                    connect = tile.connects[i]
                    if connect is not None:
                        continue
                    connect2 = tile2.connects[j]
                    if connect2 is not None:
                        continue
                    if (tile.tid, tile2.tid) in matched or (tile2.tid, tile.tid) in matched:
                        continue
                    bord2 = borders2[j]
                    if bord1 == bord2[::-1]:
                        while tile2.get_borders()[(i+2)%4] != bord2:
                            tile2.rotate_left(set())
                        if tile.get_borders()[i] != tile2.get_borders()[(i+2)%4][::-1]:
                            p('ERROR')
                        tile.connects[i] = tile2
                        tile2.connects[(i+2)%4] = tile
                        matched.add((tile.tid, tile2.tid))
                        skip = True
                        break
                    elif bord1 == bord2:
                        while tile2.get_borders()[(i+2)%4] != bord2:
                            tile2.rotate_left(set())
                        if i%2==0:
                            tile2.mirror_vertical(set())
                        else:
                            tile2.mirror_horizontal(set())
                        tile.connects[i] = tile2
                        tile2.connects[(i+2)%4] = tile
                        matched.add((tile.tid, tile2.tid))
                        skip = True
                        break

    while tile.connects[1] != None:
        tile = tile.connects[1]

    while tile.connects[0] != None:
        tile = tile.connects[0]

    board = merge_tiles(tile)
    p(find_pattern(board))
    
if __name__ == '__main__':
    main()
