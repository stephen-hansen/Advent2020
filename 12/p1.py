from utils import *
import re
import copy

def rotate_left(d):
    m = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    return m[d]

def rotate_right(d):
    m = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    return m[d]

def main():
    # Load all lines
    lines = getlines()
    d = 'E'
    spos = [0, 0]
    pos = spos
    for l in lines:
        path = l[0]
        n = int(l[1:])
        if path == 'N':
            pos[0] += n
        elif path == 'S':
            pos[0] -= n
        elif path == 'E':
            pos[1] += n
        elif path == 'W':
            pos[1] -= n
        elif path == 'L':
            for i in range(n//90):
                d = rotate_left(d)
        elif path == 'R':
            for i in range(n//90):
                d = rotate_right(d)
        elif path == 'F':
            if d == 'N':
                pos[0] += n
            elif path == 'S':
                pos[0] -= n
            elif path == 'E':
                pos[1] += n
            elif path == 'W':
                pos[1] -= n
    print(abs(pos[0]) + abs(pos[1]))

if __name__ == '__main__':
    main()
