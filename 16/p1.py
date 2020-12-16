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
    while i < len(lines):
        l = lines[i]
        tikz.append(list(map(int, l.split(','))))
        i += 1
    ninvalid = 0
    for t in tikz:
        for q in t:
            valid = False
            for k, v in fields.items():
                for r in v:
                    a = r[0]
                    b = r[1]
                    if a <= q <= b:
                        valid = True
            if not valid:
                p(q)
                ninvalid += q
    p(ninvalid)

        
if __name__ == '__main__':
    main()
