from utils import *
import re
import copy
from functools import *
from collections import *

def main():
    # Load all lines
    lines = getlines()
    fields = {}
    i = 0
    while True:
        l = lines[i].split(':')
        k = l[0]
        if len(l) != 2:
            break
        v = l[1].strip().split(' or ')
        v = list(map(lambda x: x.split('-'), v))
        v = [ list(map(int, j)) for j in v ]
        fields[k] = v
        i += 1
    i += 2
    y_t = list(map(int, lines[i].split(',')))
    i += 3
    tikz = []
    newtikz = []
    while i < len(lines):
        l = lines[i]
        tikz.append(list(map(int, l.split(','))))
        i += 1
    ninvalid = 0
    for t in tikz:
        is_valid = True
        for q in t:
            valid = False
            for k, v in fields.items():
                for r in v:
                    a = r[0]
                    b = r[1]
                    if a <= q <= b:
                        valid = True
            if not valid:
                is_valid = False
                break
        if not is_valid:
            continue
        newtikz.append(t)
    possible = []
    for i in range(len(y_t)):
        c = set()
        for k in fields:
            c.add(k)
        possible.append(c)
    for t in newtikz:
        for i in range(len(t)):
            q = t[i]
            for k, v in fields.items():
                valid = False
                for r in v:
                    a = r[0]
                    b = r[1]
                    if a <= q <= b:
                        valid = True
                if not valid and k in possible[i]:
                    possible[i].remove(k)

    while True:
        counts = defaultdict(int)
        for i in range(len(possible)):
            for k in possible[i]:
                counts[k] += 1
        for k, v in counts.items():
            if v == 1:
                for i in range(len(possible)):
                    for k2 in list(possible[i]):
                        if k2 != k and k in possible[i]:
                            possible[i].remove(k2)
        can_end = True
        for k in possible:
            if len(k) != 1:
                can_end = False
        if can_end:
            break

    maps = {}
    for i in range(len(possible)):
        for k in possible[i]:
            maps[k] = i
    p(maps)
    t = 1
    for k, i in maps.items():
        if k.startswith('departure'):
            t *= y_t[i]
    p(t)

        
if __name__ == '__main__':
    main()
